# Playwright Python QA Framework

Production-style QA automation framework built with **Playwright + Pytest + Python**.

The project demonstrates a scalable automation architecture covering:

- UI testing
- API testing
- End-to-end flows
- CI/CD automation
- Parallel execution
- Reusable framework components

---

## Tech Stack

- Python
- Playwright
- Pytest
- Pytest Playwright
- Requests
- Pytest-xdist
- Allure
- GitHub Actions

---

## Framework Architecture

### Core Components

```text
pages/
├── base_page.py
├── login_page.py
├── products_page.py
├── cart_page.py
└── checkout_page.py

tests/
├── api/
├── ui/
└── e2e/

fixtures/
├── page_objects.py

utils/
├── api_client.py
├── api_assertions.py
└── config.py

data/
├── users.py
└── api_payloads.py
```

### Key Design Patterns

- Page Object Model (POM)
- BasePage inheritance
- Reusable fixtures
- Configuration layer
- Data-driven testing
- API abstraction layer
- Reusable assertions

---

## Test Coverage

### UI Tests

- Login validation
- Negative authentication scenarios
- Cart functionality
- Checkout validation
- Smoke suite

### API Tests

- GET requests
- POST requests
- DELETE requests
- API response validation

### E2E Tests

- Complete purchase flow

---

## Features

- UI + API + E2E testing
- Parallel execution (`pytest-xdist`)
- Environment configuration support
- Screenshots on failure
- Video recording on failure
- Playwright tracing
- Authenticated fixture setup
- CI/CD pipeline with GitHub Actions

---

## Installation

Clone repository:

```bash
git clone https://github.com/DonatAQA/playwright-python-qa-framework.git
cd playwright-python-qa-framework
```

Create virtual environment:

```bash
python -m venv .venv
```

Activate environment:

Windows:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Install Playwright browsers:

```bash
playwright install
```

---

## Run Tests

Run full suite:

```bash
pytest
```

Run smoke suite:

```bash
pytest -m smoke
```

Run UI tests:

```bash
pytest -m ui
```

Run API tests:

```bash
pytest -m api
```

Run E2E tests:

```bash
pytest -m e2e
```

---

## Reporting

The framework supports:

- Allure result generation
- Screenshots on failure
- Video recording
- Playwright traces

Generate Allure results:

```bash
pytest
```

Results directory:

```text
reports/allure-results
```

---

## Parallel Execution

Parallel execution is enabled using **pytest-xdist**.

Example:

```bash
pytest -n auto
```

---

## CI/CD

GitHub Actions pipeline automatically runs on:

- push
- pull_request

Pipeline includes:

- dependency installation
- Playwright browser installation
- automated test execution