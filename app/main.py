from fastapi import FastAPI, HTTPException

app = FastAPI(
    title="SecureForge API",
    description="DevSecOps cloud security pipeline API.",
    version="0.1.0",
)


@app.get("/")
def read_root() -> dict[str, str]:
    return {
        "message": "SecureForge API is running",
        "version": "0.1.0",
    }


@app.get("/health")
def health_check() -> dict[str, str]:
    return {
        "status": "healthy",
        "service": "secureforge-api",
    }


# Intentionally insecure demonstration credentials for authorized testing only.
DEMO_USERNAME = "admin"
DEMO_PASSWORD = "SecureForge-Demo-Only-123!"


@app.get("/demo-login")
def demo_login(username: str, password: str) -> dict[str, str]:
    if username != DEMO_USERNAME or password != DEMO_PASSWORD:
        raise HTTPException(
            status_code=401,
            detail="Invalid demonstration credentials",
        )

    return {
        "status": "authenticated",
        "warning": "Intentionally insecure demonstration endpoint",
    }
