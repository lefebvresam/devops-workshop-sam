# Debugging the API

The Dev Container starts the API in the `workspace` service under `debugpy`. VS Code attaches to it using the `Attach to API (debugpy)` launch configuration. The API listens on port `8000`; the debugger listens on port `5678`.

## Start

1. In VS Code, run **Dev Containers: Reopen in Container**. The first time, or after changing the Dev Container image or Compose configuration, run **Dev Containers: Rebuild and Reopen in Container** so the image includes the pinned development dependencies, including `debugpy`.
2. Wait for the workspace container to start. It starts the API and debug listener automatically; `devcontainer.json` forwards ports `8000` and `5678`.
3. Open **Run and Debug**, select **Attach to API (debugpy)**, and press `F5`.

## Verify

1. Set a breakpoint in `backend/app/main.py`, for example inside `health()`.
2. From a terminal in the Dev Container, request the API running under the debugger:

   ```bash
   curl --fail --silent --show-error http://localhost:8000/api/health
   ```

   The response should be `{"status":"ok"}`, and VS Code should pause at the breakpoint.

Use port `8000` to verify the debugged API. The frontend at `http://localhost:8080` proxies requests to the separate Compose `backend` service, not the API in `workspace`.

## Stop

- Press `Shift+F5` (or click **Stop**) to disconnect the debugger. Because this is an attach configuration, the API and debug listener keep running in the workspace container; you can attach again later.
- To stop the API and the Compose services, run **Dev Containers: Reopen Folder Locally** or close the Dev Container window. The configured `shutdownAction` stops the Compose stack. Reopen the project in the Dev Container to start it again.