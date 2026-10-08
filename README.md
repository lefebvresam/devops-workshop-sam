# My DevOps workshop page

This repository started as a small Hello World page created during the VIVES DevOps workshop.

## Run with Docker Compose

The page (`frontend`, nginx) and the Python API (`backend`, FastAPI) run as two containers. Run every command from the project folder.

### Start

~~~bash
docker compose up --build -d --wait
~~~

This builds both images, starts the containers in the background and waits until the backend reports healthy. Open the page on port `8080` through VS Code's **Ports** view, or at `http://localhost:8080` on the LXC container.

Check that both services are running:

~~~bash
docker compose ps
~~~

The backend should show `(healthy)`.

### Logs

~~~bash
docker compose logs -f
~~~

Follow only one service:

~~~bash
docker compose logs -f backend
docker compose logs -f frontend
~~~

Press `Ctrl+C` to stop following. The containers keep running.

### Health check

~~~bash
curl --fail --silent --show-error http://localhost:8080/api/health
~~~

Expected output: `{"status":"ok"}`. This request goes through the frontend, so it checks both containers and the proxy between them.

Run the full check of all API endpoints through the frontend:

~~~bash
./scripts/verify.sh
~~~

Show the workshop label and the API's Python version:

~~~bash
curl --fail --silent --show-error http://localhost:8080/api/workshop-info
~~~

### Shut down

~~~bash
docker compose down
~~~

This stops and removes both containers and their network. Your files and the built images stay.

## View the page without Docker

From the project folder, run:

~~~bash
python3 -m http.server 8000 --bind 127.0.0.1
~~~

Then use VS Code's **Ports** view to open the forwarded port in a browser.

## Project boundaries

- The page contains only safe, non-confidential example content.
- It uses plain HTML, CSS and JavaScript.
- It has no external dependencies or network requests.

## Security checks

Pull requests to `main` must pass these checks:

| Check | Workflow | Why it is required |
|---|---|---|
| `verify-python-api` | `verify.yml` | Fast and deterministic; runs the API's syntax check and tests. |
| `workshop-policy` | `quality-gate.yml` | Takes seconds; rejects the workshop training marker, which no other check covers. |
| `dependency-review` | `dependency-review.yml` | Fast and only runs on pull requests; blocks new dependencies with high-severity vulnerabilities. |

These checks are deliberately not required:

- `smoke-test` runs only when started by hand and depends on one self-hosted runner.
- `deployment-handoff` runs only after a merge to `main`, so it never reports on a pull request.

GitHub secret scanning with push protection and Dependabot alerts are enabled in the repository settings. Dependabot also proposes weekly updates for the pinned Python packages and the GitHub Actions versions.

If a real credential leaks, follow [Responding to a leaked credential](docs/credential-response.md). Record any temporary exception in [Security exceptions](docs/security-exceptions.md).

## Main file

[Open the page](index.html)

~~~markdown
This page is a small, team and personal oriented example of a shared software project.
~~~

test