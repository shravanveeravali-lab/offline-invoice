# Security Policy

## Supported Versions

| Version | Supported |
| ------- | --------- |
| 0.1.x | Yes |

## Security Model

Offline Invoice Intelligence System is designed as a local-first application. Uploaded invoice files, extracted text, structured JSON, and SQLite records are intended to remain on the user's machine.

The system must not send invoice content to cloud AI services or external OCR providers.

## Data Sensitivity

Invoices may contain:

- Vendor names
- Customer names
- Addresses
- Tax identifiers
- GST details
- Bank details
- Pricing and payment information

Use synthetic samples for development, testing, and demos.

## Prohibited Security Regressions

- Adding OpenAI, Gemini, Anthropic, Claude, Groq, or other cloud AI APIs.
- Sending invoice data to external OCR services.
- Adding telemetry that transmits document content.
- Committing real invoice files.
- Committing secrets, keys, tokens, or credentials.
- Requiring internet access at runtime.

## Reporting a Vulnerability

Report vulnerabilities privately to the maintainers. Include:

- Summary
- Impact
- Steps to reproduce
- Affected version or commit
- Suggested mitigation, if known

## Recommended Security Checks

- Secret scanning
- Dependency vulnerability scanning
- Static analysis
- License review
- Manual review for network calls
- Offline execution validation

## Local Hardening Recommendations

- Bind local servers to `127.0.0.1`.
- Store sample data separately from real invoices.
- Keep the SQLite database in a user-controlled local directory.
- Remove demo data before sharing screenshots or recordings.
- Verify model files come from trusted open-source sources.
