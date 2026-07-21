from fastapi.testclient import TestClient
from pytest import MonkeyPatch

from app.main import app


client = TestClient(app)


def test_read_root() -> None:
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "message": "SecureForge API is running",
        "version": "0.1.0",
    }


def test_health_check() -> None:
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {
        "status": "healthy",
        "service": "secureforge-api",
    }


def test_demo_login_success(monkeypatch: MonkeyPatch) -> None:
    monkeypatch.setenv("DEMO_USERNAME", "admin")
    monkeypatch.setenv("DEMO_PASSWORD", "SecureForge-Demo-Only-123!")

    response = client.get(
        "/demo-login",
        params={
            "username": "admin",
            "password": "SecureForge-Demo-Only-123!",
        },
    )

    assert response.status_code == 200
    assert response.json() == {
        "status": "authenticated",
        "warning": "Demonstration endpoint using environment configuration",
    }


def test_demo_login_rejects_invalid_credentials(
    monkeypatch: MonkeyPatch,
) -> None:
    monkeypatch.setenv("DEMO_USERNAME", "admin")
    monkeypatch.setenv("DEMO_PASSWORD", "SecureForge-Demo-Only-123!")

    response = client.get(
        "/demo-login",
        params={
            "username": "admin",
            "password": "wrong-password",
        },
    )

    assert response.status_code == 401
    assert response.json() == {
        "detail": "Invalid demonstration credentials",
    }


def test_demo_login_requires_configuration(
    monkeypatch: MonkeyPatch,
) -> None:
    monkeypatch.delenv("DEMO_USERNAME", raising=False)
    monkeypatch.delenv("DEMO_PASSWORD", raising=False)

    response = client.get(
        "/demo-login",
        params={
            "username": "admin",
            "password": "anything",
        },
    )

    assert response.status_code == 503
    assert response.json() == {
        "detail": "Demonstration credentials are not configured",
    }
