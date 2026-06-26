# Playwright Python Automation Suite

An end-to-end UI automation testing project built using **Python**, **Playwright (Sync API)**, and **Pytest**. This project automates core user workflows on the SauceDemo application while demonstrating modern QA automation concepts such as fixtures, parameterized testing, custom markers, and test reporting.

---

# Tech Stack

* Python
* Playwright (Sync API)
* Pytest
* Pytest HTML
* Allure Reports

---

# Automated Test Cases

* ✅ Valid Login
* ✅ Invalid Login Validation (Parameterized)
* ✅ Add Single Item to Cart
* ✅ Add Multiple Items to Cart
* ✅ Complete Checkout Flow

---

# Features

* Pytest Fixtures
* Parameterized Testing
* Custom Markers
* Assertions
* HTML Report Generation
* Allure Report Generation
* Automated Setup & Teardown

---

# Project Structure

```text
AutoTests/
│
├── reports/
│   ├── allure-results/
│   ├── assets/
│   └── AutomationReport.html
│
├── tests/
│   └── test_suite.py
│
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

---

# Installation

Clone the repository:

```bash
git clone <repository-url>
cd AutoTests
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

# Running Tests

Run the complete suite:

```bash
pytest
```

Run cart-related tests only:

```bash
pytest -m testCart
```

---

# Reports

HTML Report:

```text
reports/AutomationReport.html
```

Generate Allure report files:

```bash
pytest --alluredir=reports/allure-results
```

View Allure Report:

```bash
allure serve reports/allure-results
```

---

# Future Improvements

* Page Object Model (POM)
* Screenshot capture on test failures
* API Automation with Python Requests
* CI/CD using GitHub Actions
* Cross-browser execution

---

## Author

**Kaustubh Shekhar**

Built as part of my journey into QA Automation using Playwright and Pytest.
