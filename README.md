# SecureForge

SecureForge is a DevSecOps cloud security pipeline designed to identify insecure code, vulnerable dependencies, exposed credentials, container vulnerabilities, and cloud infrastructure misconfigurations before deployment.

## Project Objective

The objective of SecureForge is to demonstrate how security controls can be integrated directly into the software development lifecycle rather than applied only after an application reaches production.

The pipeline will automatically evaluate source code, application dependencies, secrets, containers, and Infrastructure as Code configurations. High-risk findings will block insecure builds and generate actionable remediation reports.

## Planned Security Capabilities

- Static application security testing
- Python dependency vulnerability scanning
- Hardcoded secret detection
- Docker container vulnerability scanning
- Terraform security scanning
- GitHub Actions security gates
- AWS cloud security monitoring
- Automated security reporting
- Incident-response playbooks
- OWASP and MITRE ATT&CK mappings

## Planned Technology Stack

- Python
- FastAPI
- GitHub Actions
- Docker
- Terraform
- AWS
- Semgrep or Bandit
- pip-audit
- Gitleaks
- Trivy
- Checkov
- Pytest

## Planned Architecture

Developer Commit
    |
    v
GitHub Repository
    |
    v
GitHub Actions Security Pipeline
    |
    +--> Source Code Scan
    +--> Dependency Scan
    +--> Secret Scan
    +--> Container Scan
    +--> Terraform Scan
    |
    v
Security Gate
    |
    +--> Pass: Allow deployment
    |
    +--> Fail: Block deployment and generate report

## Repository Structure

secureforge-devsecops/
├── .github/
│   └── workflows/
├── app/
├── docs/
├── reports/
├── scripts/
├── security/
├── terraform/
├── tests/
├── CHANGELOG.md
├── CONTRIBUTING.md
├── SECURITY.md
├── pyproject.toml
├── requirements-dev.txt
└── requirements.txt

## Development Roadmap

### Phase 1 — Application Foundation

- Create the FastAPI application
- Add health-check and demonstration endpoints
- Add unit tests
- Containerize the application

### Phase 2 — DevSecOps Pipeline

- Add static-code scanning
- Add dependency scanning
- Add secret detection
- Add container scanning
- Add security gates to GitHub Actions

### Phase 3 — Cloud Security

- Build AWS infrastructure with Terraform
- Detect Infrastructure as Code misconfigurations
- Enable AWS security logging
- Analyze CloudTrail security events

### Phase 4 — Detection and Incident Response

- Detect suspicious AWS activity
- Map detections to MITRE ATT&CK
- Generate incident reports
- Create remediation playbooks

## Current Status

Day 1: Repository initialized and project structure created.

## Disclaimer

This project is intended exclusively for defensive cybersecurity education, controlled testing, and portfolio development.

## License

This project is licensed under the MIT License.

## Running the Application

Install the project dependencies:

```bash
pip install -r requirements.txt -r requirements-dev.txt
```

Start the FastAPI development server:

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

Available endpoints:

- `GET /` — confirms that the SecureForge API is running
- `GET /health` — returns the service health status
- `GET /docs` — opens the interactive Swagger API documentation

## Running Tests

Run the automated test suite:

```bash
python -m pytest -v
```

## Current Progress

- Day 1: Initialized the repository and project structure
- Day 2: Built the FastAPI foundation, health endpoint, and automated tests


## Security Demonstration Endpoint

SecureForge includes an intentionally insecure authentication endpoint for authorized security testing.

- `GET /demo-login`
- Uses fake hardcoded demonstration credentials
- Returns `200 OK` for valid credentials
- Returns `401 Unauthorized` for invalid credentials
- Will be scanned and remediated in a future security-pipeline phase

> Warning: This endpoint is deliberately insecure and must never be used in a production environment.
