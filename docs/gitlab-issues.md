# GitLab Issues

## Issue 1: Finalize Project Specification

**Description:** Create a complete specification covering problem statement, vision, objectives, scope, requirements, constraints, risks, and acceptance criteria.

**Assignee:** Shravan

**Priority:** High

**Estimate:** 2 hours

**Due Date:** 2026-06-28

**Acceptance Criteria:**

- `spec.md` exists under `specs/001-offline-invoice-intelligence/`.
- Specification includes all Phase 1 required sections.
- Offline and CPU-only constraints are clearly documented.

**Dependencies:** None

## Issue 2: Create Architecture Plan

**Description:** Document the application architecture, workflow, technology stack, implementation plan, testing strategy, deployment strategy, and risk mitigation.

**Assignee:** Shravan

**Priority:** High

**Estimate:** 3 hours

**Due Date:** 2026-06-28

**Acceptance Criteria:**

- `plan.md` includes ASCII architecture diagram.
- Workflow is documented end to end.
- Technology decisions are clearly explained.

**Dependencies:** Issue 1

## Issue 3: Research OCR Approach

**Description:** Research OCR requirements for invoice images and PDFs, including strengths and limitations.

**Assignee:** Pratham

**Priority:** High

**Estimate:** 2 hours

**Due Date:** 2026-06-28

**Acceptance Criteria:**

- OCR research is included in `research.md`.
- Invoice-specific OCR challenges are documented.
- Offline OCR requirement is addressed.

**Dependencies:** Issue 1

## Issue 4: Research Tesseract OCR

**Description:** Document why Tesseract OCR is selected for local text extraction.

**Assignee:** Pratham

**Priority:** High

**Estimate:** 2 hours

**Due Date:** 2026-06-28

**Acceptance Criteria:**

- Tesseract benefits and limitations are documented.
- Offline and CPU compatibility are explained.
- Alternatives are briefly compared.

**Dependencies:** Issue 3

## Issue 5: Research TinyLlama GGUF

**Description:** Document TinyLlama GGUF as the local model choice for structured invoice extraction.

**Assignee:** Pratham

**Priority:** High

**Estimate:** 2 hours

**Due Date:** 2026-06-29

**Acceptance Criteria:**

- TinyLlama rationale is documented.
- GGUF compatibility is mentioned.
- Model limitations and validation needs are included.

**Dependencies:** Issue 2

## Issue 6: Research llama.cpp Runtime

**Description:** Document llama.cpp as the CPU-first local AI runtime.

**Assignee:** Pratham

**Priority:** High

**Estimate:** 2 hours

**Due Date:** 2026-06-29

**Acceptance Criteria:**

- llama.cpp role is documented.
- CPU-only inference benefits are explained.
- GGUF support is included.

**Dependencies:** Issue 5

## Issue 7: Document SQLite Data Model

**Description:** Create the data model document covering invoices, invoice items, and processing logs.

**Assignee:** Shravan

**Priority:** High

**Estimate:** 3 hours

**Due Date:** 2026-06-29

**Acceptance Criteria:**

- `data-model.md` exists.
- ER diagram is included.
- Tables and relationships are documented.

**Dependencies:** Issue 1

## Issue 8: Define Invoice JSON Schema

**Description:** Document the expected structured JSON output for invoice extraction.

**Assignee:** Shravan

**Priority:** High

**Estimate:** 2 hours

**Due Date:** 2026-06-29

**Acceptance Criteria:**

- JSON schema includes vendor, invoice number, date, currency, GST, items, subtotal, total, and confidence score.
- Example JSON is included.
- Field types and required fields are clear.

**Dependencies:** Issue 7

## Issue 9: Create Team Task Breakdown

**Description:** Create a detailed task plan split between Shravan and Pratham.

**Assignee:** Shravan

**Priority:** High

**Estimate:** 2 hours

**Due Date:** 2026-06-29

**Acceptance Criteria:**

- `tasks.md` exists.
- Each task includes assignee, priority, estimate, dependencies, and status.
- Shared tasks are identified.

**Dependencies:** Issue 1

## Issue 10: Rewrite Professional README

**Description:** Rewrite README for GitLab repository review and hackathon submission.

**Assignee:** Shravan

**Priority:** High

**Estimate:** 3 hours

**Due Date:** 2026-06-29

**Acceptance Criteria:**

- README includes project description, architecture, features, installation, offline setup, running, folder structure, API documentation, screenshots placeholder, demo instructions, future scope, license, and contributors.
- README clearly states no cloud AI APIs are used.
- Mermaid architecture diagram is included.

**Dependencies:** Issue 2

## Issue 11: Create Contributing Guide

**Description:** Write contribution guidelines for documentation, development workflow, review expectations, privacy, and offline constraints.

**Assignee:** Shravan

**Priority:** Medium

**Estimate:** 1 hour

**Due Date:** 2026-06-29

**Acceptance Criteria:**

- `CONTRIBUTING.md` exists.
- Offline-first contribution rules are documented.
- Merge request checklist is included.

**Dependencies:** None

## Issue 12: Create Security Policy

**Description:** Write security policy covering data privacy, vulnerability reporting, prohibited regressions, and local hardening.

**Assignee:** Pratham

**Priority:** High

**Estimate:** 2 hours

**Due Date:** 2026-06-29

**Acceptance Criteria:**

- `SECURITY.md` exists.
- Sensitive invoice data risks are documented.
- No-cloud and no-telemetry constraints are explicit.

**Dependencies:** Issue 1

## Issue 13: Create Code of Conduct

**Description:** Add project code of conduct for respectful collaboration and privacy-aware teamwork.

**Assignee:** Shravan

**Priority:** Medium

**Estimate:** 1 hour

**Due Date:** 2026-06-29

**Acceptance Criteria:**

- `CODE_OF_CONDUCT.md` exists.
- Expected and unacceptable behaviors are listed.
- Reporting process is included.

**Dependencies:** None

## Issue 14: Create Changelog

**Description:** Create initial changelog for documentation and planning milestones.

**Assignee:** Shravan

**Priority:** Medium

**Estimate:** 1 hour

**Due Date:** 2026-06-29

**Acceptance Criteria:**

- `CHANGELOG.md` exists.
- Initial version is documented.
- Added documentation artifacts are listed.

**Dependencies:** None

## Issue 15: Create Roadmap

**Description:** Create roadmap describing Phase 1 through future improvements.

**Assignee:** Shravan

**Priority:** Medium

**Estimate:** 2 hours

**Due Date:** 2026-06-29

**Acceptance Criteria:**

- `ROADMAP.md` exists.
- Phases include planning, MVP, offline demo readiness, reliability, and packaging.
- Future scope is documented.

**Dependencies:** Issue 1

## Issue 16: Create Architecture Documentation

**Description:** Create architecture document with system diagram, workflow, ER diagram, folder structure, and deployment model.

**Assignee:** Shravan

**Priority:** High

**Estimate:** 3 hours

**Due Date:** 2026-06-29

**Acceptance Criteria:**

- `ARCHITECTURE.md` exists.
- Mermaid system architecture diagram is included.
- Mermaid workflow and ER diagrams are included.
- Offline boundary is documented.

**Dependencies:** Issue 2, Issue 7

## Issue 17: Document Offline Demo Procedure

**Description:** Document how to demonstrate the system with Wi-Fi disabled.

**Assignee:** Pratham

**Priority:** High

**Estimate:** 2 hours

**Due Date:** 2026-06-30

**Acceptance Criteria:**

- Demo steps are included in README or dedicated documentation.
- Local dependency preparation is documented.
- No internet runtime dependency is emphasized.

**Dependencies:** Issue 10

## Issue 18: Document API Endpoints

**Description:** Document REST API endpoints for upload, extraction, invoice retrieval, history, and deletion.

**Assignee:** Pratham

**Priority:** High

**Estimate:** 2 hours

**Due Date:** 2026-06-30

**Acceptance Criteria:**

- API endpoint table exists.
- Each endpoint has a clear purpose.
- Request and response expectations are described.

**Dependencies:** Issue 2

## Issue 19: Add Mermaid Folder Structure Diagram

**Description:** Add a Mermaid diagram showing repository folder structure.

**Assignee:** Shravan

**Priority:** Medium

**Estimate:** 1 hour

**Due Date:** 2026-06-30

**Acceptance Criteria:**

- Folder structure diagram appears in README or architecture docs.
- Specs folder is represented.
- Backend, frontend, docs, and samples folders are represented.

**Dependencies:** Issue 10

## Issue 20: Document CPU Optimization Strategy

**Description:** Document how the project remains practical for CPU-only laptops.

**Assignee:** Pratham

**Priority:** High

**Estimate:** 2 hours

**Due Date:** 2026-06-30

**Acceptance Criteria:**

- CPU optimization section exists in research or plan documentation.
- Quantized GGUF, prompt limits, OCR cleaning, and caching are covered.
- CUDA and GPU exclusion is documented.

**Dependencies:** Issue 6

## Issue 21: Prepare Screenshot Placeholders

**Description:** Add placeholders for dashboard, upload flow, extracted invoice, history, and offline demo screenshots.

**Assignee:** Shravan

**Priority:** Low

**Estimate:** 1 hour

**Due Date:** 2026-06-30

**Acceptance Criteria:**

- Screenshot placeholder section exists in README.
- Required screenshot list is clear.
- No real sensitive invoice data is included.

**Dependencies:** Issue 10

## Issue 22: Validate AGPL-3.0 License Documentation

**Description:** Confirm license documentation and README references align with AGPL-3.0-or-later.

**Assignee:** Shravan

**Priority:** High

**Estimate:** 1 hour

**Due Date:** 2026-06-30

**Acceptance Criteria:**

- README references AGPL-3.0.
- License file exists.
- SPDX identifier is documented.

**Dependencies:** None

## Issue 23: Final Documentation Review

**Description:** Review all documentation for completeness, consistency, and hackathon Phase 1 compliance.

**Assignee:** Shared

**Priority:** High

**Estimate:** 3 hours

**Due Date:** 2026-06-30

**Acceptance Criteria:**

- All required files exist.
- No application source code was generated as part of documentation-only work.
- Offline-first and CPU-only requirements are consistent across documents.
- GitLab repository is ready for review.

**Dependencies:** Issue 1 through Issue 22
