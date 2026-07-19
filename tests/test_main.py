from fastapi.testclient import TestClient

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


def test_demo_login_success() -> None:
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
        "warning": "Intentionally insecure demonstration endpoint",
    }


def test_demo_login_rejects_invalid_credentials() -> None:
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
