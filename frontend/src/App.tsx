import { FileSearch, RefreshCw, Search, Trash2, UploadCloud } from "lucide-react";
import { FormEvent, useCallback, useEffect, useMemo, useState } from "react";

import { Invoice, deleteInvoice, extractInvoice, fetchHistory, uploadInvoice } from "./api";

function money(value: number, currency: string): string {
  return new Intl.NumberFormat("en-IN", {
    style: "currency",
    currency,
    maximumFractionDigits: 2,
  }).format(value);
}

export default function App() {
  const [file, setFile] = useState<File | null>(null);
  const [invoices, setInvoices] = useState<Invoice[]>([]);
  const [selected, setSelected] = useState<Invoice | null>(null);
  const [query, setQuery] = useState("");
  const [status, setStatus] = useState("Ready for offline extraction");
  const [busy, setBusy] = useState(false);

  const totals = useMemo(
    () => ({
      count: invoices.length,
      value: invoices.reduce((sum, invoice) => sum + invoice.total, 0),
      averageConfidence:
        invoices.length === 0
          ? 0
          : invoices.reduce((sum, invoice) => sum + invoice.confidence_score, 0) / invoices.length,
    }),
    [invoices],
  );

  const refresh = useCallback(async (nextQuery = query) => {
    const history = await fetchHistory(nextQuery);
    setInvoices(history);
    setSelected((current) => current ?? history[0] ?? null);
  }, [query]);

  useEffect(() => {
    refresh().catch((error) => setStatus(error.message));
  }, [refresh]);

  async function handleSubmit(event: FormEvent) {
    event.preventDefault();
    if (!file) {
      setStatus("Choose an invoice PDF, image, or sample text file");
      return;
    }
    setBusy(true);
    try {
      setStatus("Uploading document locally");
      const uploaded = await uploadInvoice(file);
      setStatus("Running OCR and local extraction");
      const invoice = await extractInvoice(uploaded.stored_path);
      await refresh();
      setSelected(invoice);
      setStatus(`Extracted ${invoice.invoice_number} from ${invoice.vendor_name}`);
    } catch (error) {
      setStatus(error instanceof Error ? error.message : "Extraction failed");
    } finally {
      setBusy(false);
    }
  }

  async function handleSearch(event: FormEvent) {
    event.preventDefault();
    await refresh(query);
  }

  async function handleDelete(id: number) {
    await deleteInvoice(id);
    setSelected(null);
    await refresh();
  }

  return (
    <main className="shell">
      <section className="topbar">
        <div>
          <p className="eyebrow">CPU-first offline AI</p>
          <h1>Invoice Intelligence</h1>
        </div>
        <form className="search" onSubmit={handleSearch}>
          <Search size={18} aria-hidden="true" />
          <input
            aria-label="Search invoices"
            placeholder="Search vendor, number, currency"
            value={query}
            onChange={(event) => setQuery(event.target.value)}
          />
          <button type="submit" title="Search">
            <FileSearch size={18} />
          </button>
        </form>
      </section>

      <section className="stats">
        <div>
          <span>Invoices</span>
          <strong>{totals.count}</strong>
        </div>
        <div>
          <span>Total Value</span>
          <strong>{money(totals.value, "INR")}</strong>
        </div>
        <div>
          <span>Avg Confidence</span>
          <strong>{Math.round(totals.averageConfidence * 100)}%</strong>
        </div>
      </section>

      <section className="workspace">
        <aside className="panel">
          <form className="upload" onSubmit={handleSubmit}>
            <label>
              <UploadCloud size={32} aria-hidden="true" />
              <span>{file ? file.name : "Drop in an invoice file"}</span>
              <input
                type="file"
                accept=".pdf,.png,.jpg,.jpeg,.tiff,.bmp,.webp,.txt"
                onChange={(event) => setFile(event.target.files?.[0] ?? null)}
              />
            </label>
            <button disabled={busy} type="submit">
              {busy ? <RefreshCw className="spin" size={18} /> : <UploadCloud size={18} />}
              Extract
            </button>
            <p>{status}</p>
          </form>

          <div className="history">
            {invoices.map((invoice) => (
              <button
                className={selected?.id === invoice.id ? "active" : ""}
                key={invoice.id}
                onClick={() => setSelected(invoice)}
                type="button"
              >
                <span>{invoice.vendor_name}</span>
                <small>
                  {invoice.invoice_number} · {money(invoice.total, invoice.currency)}
                </small>
              </button>
            ))}
          </div>
        </aside>

        <section className="detail">
          {selected ? (
            <>
              <header>
                <div>
                  <p className="eyebrow">{selected.invoice_number}</p>
                  <h2>{selected.vendor_name}</h2>
                </div>
                <button
                  className="icon danger"
                  onClick={() => handleDelete(selected.id)}
                  title="Delete invoice"
                  type="button"
                >
                  <Trash2 size={18} />
                </button>
              </header>
              <dl className="facts">
                <div>
                  <dt>Date</dt>
                  <dd>{selected.invoice_date}</dd>
                </div>
                <div>
                  <dt>GST</dt>
                  <dd>{money(selected.gst, selected.currency)}</dd>
                </div>
                <div>
                  <dt>Total</dt>
                  <dd>{money(selected.total, selected.currency)}</dd>
                </div>
                <div>
                  <dt>Confidence</dt>
                  <dd>{Math.round(selected.confidence_score * 100)}%</dd>
                </div>
              </dl>
              <table>
                <thead>
                  <tr>
                    <th>Item</th>
                    <th>Qty</th>
                    <th>Price</th>
                    <th>Subtotal</th>
                  </tr>
                </thead>
                <tbody>
                  {selected.items.map((item) => (
                    <tr key={`${selected.id}-${item.description}`}>
                      <td>{item.description}</td>
                      <td>{item.quantity}</td>
                      <td>{money(item.price, selected.currency)}</td>
                      <td>{money(item.subtotal, selected.currency)}</td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </>
          ) : (
            <div className="empty">Upload or select an invoice to review extracted fields.</div>
          )}
        </section>
      </section>
    </main>
  );
}
