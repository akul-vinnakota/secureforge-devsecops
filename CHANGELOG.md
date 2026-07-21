# Changelog

All significant changes to SecureForge will be documented in this file.

## [Unreleased]

### Added

- Remediated the Bandit B105 hardcoded credential finding using environment variables
- Added secure missing-configuration handling with an HTTP 503 response
- Added an `.env.example` template with public placeholders
- Expanded automated test coverage to five tests

- Bandit static application security scanning
- Reusable security scan script with JSON reporting
- GitHub Actions workflow for automated tests and security scans
- CI security gate that fails when vulnerabilities are detected

- Controlled insecure demonstration login endpoint
- Authentication success and failure tests
- Documentation for authorized security testing

- FastAPI application foundation
- Root and health-check API endpoints
- Automated pytest coverage for API endpoints

### Planned

- FastAPI application foundation
- Automated unit testing
- Static application security testing
- Dependency vulnerability scanning
- Secret detection
- Docker security scanning
- Terraform security scanning
- GitHub Actions security gates
- AWS logging and detection capabilities

## [0.1.0] - 2026-07-15

### Added

- Initial GitHub repository
- Professional project README
- Security policy
- Contribution guidelines
- Initial repository structure
- Development roadmap
