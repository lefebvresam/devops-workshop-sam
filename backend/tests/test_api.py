import platform

from app.main import health, release_info, welcome, workshop_info, workshop_version_info


def test_health() -> None:
    assert health() == {"status": "ok"}


def test_welcome_uses_a_default_team_name(monkeypatch) -> None:
    monkeypatch.delenv("WORKSHOP_TEAM_NAME", raising=False)

    assert welcome()["team"] == "Workshop team"


def test_workshop_version_info_uses_a_default_label(monkeypatch) -> None:
    monkeypatch.delenv("WORKSHOP_LABEL", raising=False)

    assert workshop_version_info() == {
        "workshop": "DevOps workshop",
        "python_version": platform.python_version(),
    }

def test_workshop_version_info_uses_the_label_from_the_environment(monkeypatch) -> None:
    monkeypatch.setenv("WORKSHOP_LABEL", "Test workshop")

    assert workshop_version_info()["workshop"] == "Test workshop"

def test_workshop_info() -> None:
    assert workshop_info() == {
        "language": "Python",
        "workspace": "Dev Container",
    }

def test_release_info_uses_defaults(monkeypatch) -> None:
    monkeypatch.delenv("WORKSHOP_RELEASE_VERSION", raising=False)
    monkeypatch.delenv("WORKSHOP_REVISION", raising=False)

    assert release_info() == {
        "status": "ok",
        "version": "dev",
        "revision": "unknown",
    }


def test_release_info_uses_configured_values(monkeypatch) -> None:
    monkeypatch.setenv("WORKSHOP_RELEASE_VERSION", " v0.1.0 ")
    monkeypatch.setenv("WORKSHOP_REVISION", " abc123 ")

    assert release_info() == {
        "status": "ok",
        "version": "v0.1.0",
        "revision": "abc123",
    }

