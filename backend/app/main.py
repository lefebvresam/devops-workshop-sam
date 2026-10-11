import os
import platform

from fastapi import FastAPI

app = FastAPI(title="Workshop Welcome Board API")


def team_name() -> str:
    return os.getenv("WORKSHOP_TEAM_NAME", "Workshop team")


def workshop_label() -> str:
    return os.getenv("WORKSHOP_LABEL", "DevOps workshop")


def release_info() -> dict[str, str]:
    version = os.getenv("WORKSHOP_RELEASE_VERSION", "").strip() or "dev"
    revision = os.getenv("WORKSHOP_REVISION", "").strip() or "unknown"
    return {
        "status": "ok",
        "version": version,
        "revision": revision,
    }


@app.get("/api/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/api/release")
def release() -> dict[str, str]:
    return release_info()


@app.get("/api/welcome")
def welcome() -> dict[str, str]:
    team = team_name()
    return {
        "message": f"Welcome, {team}!",
        "team": team,
    }


@app.get("/api/workshop-version-info")
def workshop_version_info() -> dict[str, str]:
    return {
        "workshop": workshop_label(),
        "python_version": platform.python_version(),
    }

@app.get("/api/workshop-info")
def workshop_info() -> dict[str, str]:
    return {
        "language": "Python",
        "workspace": "Dev Container",
    }
