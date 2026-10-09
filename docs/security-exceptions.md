# Security exceptions

Any temporary exception to a security check (an ignored alert, an allowlisted scanner finding, a check removed from the `main` ruleset) must have a row in this table. An exception without a row here is not approved.

| Exception | Reason | Owner | Review cadence | Expires |
|---|---|---|---|---|
| _None_ | | | | |

## Rules

- **Owner** is a named person, not a team, who is responsible for removing or renewing the exception.
- **Review cadence** is how often the owner checks whether the exception is still needed, for example monthly.
- **Expires** is a date at most three months away. On that date, remove the exception or renew it with a new date and a reason.
- Link the row from the place where the exception is configured, for example in a comment next to a scanner allowlist entry or in the alert's dismissal note.
