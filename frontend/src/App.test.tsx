import { render, screen } from "@testing-library/react";
import { describe, expect, it, vi } from "vitest";

import App from "./App";

vi.mock("./api", () => ({
  fetchHistory: () => Promise.resolve([]),
  uploadInvoice: vi.fn(),
  extractInvoice: vi.fn(),
  deleteInvoice: vi.fn(),
}));

describe("App", () => {
  it("renders the dashboard title", async () => {
    render(<App />);
    expect(await screen.findByText("Invoice Intelligence")).toBeInTheDocument();
  });
});
