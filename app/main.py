import os

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


@app.get("/demo-login")
def demo_login(username: str, password: str) -> dict[str, str]:
    demo_username = os.getenv("DEMO_USERNAME")
    demo_password = os.getenv("DEMO_PASSWORD")

    if not demo_username or not demo_password:
        raise HTTPException(
            status_code=503,
            detail="Demonstration credentials are not configured",
        )

    if username != demo_username or password != demo_password:
        raise HTTPException(
            status_code=401,
            detail="Invalid demonstration credentials",
        )

    return {
        "status": "authenticated",
        "warning": "Demonstration endpoint using environment configuration",
    }
