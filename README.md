# traceability-demo-store

Demo repository for the **Requirements Traceability** GitHub App.

| File | What it is |
|---|---|
| `docs/SRS.docx` | IEEE 830 software requirements specification (REQ-01 … REQ-10) |
| `openapi.yaml` | OpenAPI 3 contract of the Nexus storefront API |
| `.traceability.yml` | Tells the bot where the SRS and the spec are, and the score thresholds |

On every pull request that changes `openapi.yaml` or `docs/SRS.docx`, the bot re-scores the changed
endpoints against the requirements. It posts a **Requirements Traceability** check run and one PR comment.
A requirement that loses alignment makes the check fail; with branch protection, that blocks the merge.
