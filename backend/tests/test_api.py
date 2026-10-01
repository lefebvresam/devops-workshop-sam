import platform

from app.main import health, welcome, workshop_info


def test_health() -> None:
    assert health() == {"status": "ok"}


def test_welcome_uses_a_default_team_name(monkeypatch) -> None:
    monkeypatch.delenv("WORKSHOP_TEAM_NAME", raising=False)

    assert welcome()["team"] == "Workshop team"


def test_workshop_info_uses_a_default_label(monkeypatch) -> None:
    monkeypatch.delenv("WORKSHOP_LABEL", raising=False)

    assert workshop_info() == {
        "workshop": "DevOps workshop",
        "python_version": platform.python_version(),
    }


def test_workshop_info_uses_the_label_from_the_environment(monkeypatch) -> None:
    monkeypatch.setenv("WORKSHOP_LABEL", "Test workshop")

    assert workshop_info()["workshop"] == "Test workshop"
