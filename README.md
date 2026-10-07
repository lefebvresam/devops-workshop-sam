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

## Main file

[Open the page](index.html)

~~~markdown
This page is a small, team and personal oriented example of a shared software project.
~~~

test