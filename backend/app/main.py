import os
import platform

from fastapi import FastAPI

app = FastAPI(title="Workshop Welcome Board API")


def team_name() -> str:
    return os.getenv("WORKSHOP_TEAM_NAME", "Workshop team")


def workshop_label() -> str:
    return os.getenv("WORKSHOP_LABEL", "DevOps workshop")


@app.get("/api/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/api/welcome")
def welcome() -> dict[str, str]:
    team = team_name()
    return {
        "message": f"Welcome, {team}!",
        "team": team,
    }


@app.get("/api/workshop-info")
def workshop_info() -> dict[str, str]:
    return {
        "workshop": workshop_label(),
        "python_version": platform.python_version(),
    }
