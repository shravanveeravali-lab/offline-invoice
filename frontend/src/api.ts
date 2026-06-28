export interface InvoiceItem {
  description: string;
  quantity: number;
  price: number;
  subtotal: number;
}

export interface Invoice {
  id: number;
  vendor_name: string;
  invoice_number: string;
  invoice_date: string;
  currency: string;
  gst: number;
  items: InvoiceItem[];
  subtotal: number;
  total: number;
  confidence_score: number;
  source_filename: string;
  created_at: string;
}

const API_BASE = import.meta.env.VITE_API_BASE ?? "http://127.0.0.1:8001";

async function request<T>(path: string, init?: RequestInit): Promise<T> {
  const response = await fetch(`${API_BASE}${path}`, init);
  if (!response.ok) {
    const detail = await response.json().catch(() => ({ detail: response.statusText }));
    throw new Error(detail.detail ?? "Request failed");
  }
  return response.json() as Promise<T>;
}

export async function uploadInvoice(file: File): Promise<{ stored_path: string; filename: string }> {
  const body = new FormData();
  body.append("file", file);
  return request("/upload", { method: "POST", body });
}

export async function extractInvoice(storedPath: string): Promise<Invoice> {
  return request("/extract", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ stored_path: storedPath }),
  });
}

export async function fetchHistory(query = ""): Promise<Invoice[]> {
  const params = query ? `?q=${encodeURIComponent(query)}` : "";
  const data = await request<{ invoices: Invoice[] }>(`/history${params}`);
  return data.invoices;
}

export async function deleteInvoice(id: number): Promise<void> {
  await request(`/invoice/${id}`, { method: "DELETE" });
}
