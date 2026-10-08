# Responding to a leaked credential

Follow these steps when a real credential (password, API key, token, private key) is committed, pushed, or shown in a CI log. Work through them in order. Start immediately: assume the credential is compromised from the moment it left your machine.

Adding the file to `.gitignore` does not fix a leak. `.gitignore` only stops untracked files from being added; the credential stays in every commit, clone, fork, and cache that already has it.

## 1. Stop the exposure

1. If the push was blocked by push protection, do not bypass it. Remove the credential from the commit before pushing again.
2. If it reached GitHub, close or convert the pull request to draft and stop any running workflows that could print it.
3. Check where else it may have been copied: forks, CI logs, workflow artifacts, issue or PR comments. Delete logs and artifacts that contain it.
4. Tell the repository owner.

## 2. Revoke or rotate the credential

1. Revoke the credential at the provider that issued it (for example the cloud console, GitHub **Settings → Developer settings**, or the service's API key page).
2. Create a new credential and store it outside the repository: a GitHub Actions secret, an environment secret, or a secret manager.
3. Update every system that used the old credential.

Do this before cleaning up history. Rewriting history does not remove copies that others already have.

## 3. Investigate its use

1. Read the provider's audit or access logs for the period between the first push and the revocation.
2. Record what was accessed, from where, and when.
3. If you find use you cannot explain, treat it as an incident and escalate to whoever owns the affected system.

## 4. Remove or remediate

1. Remove the credential from the code and read it from the environment or a secret store instead.
2. If the credential appears in history, decide with the owner whether to rewrite history (for example with `git filter-repo`). After rotation, the old value is useless, so rewriting is optional cleanup, not the fix.
3. Close the related secret scanning alert in **Security → Secret scanning** with the reason **Revoked**.
4. Write down what happened and what prevents it next time, for example a new scanner rule or a change to how secrets are loaded.
