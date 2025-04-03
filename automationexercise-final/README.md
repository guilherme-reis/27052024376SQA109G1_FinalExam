# AutomationExercise Test Suite

This test suite automates user registration, login, and account deletion on [AutomationExercise](https://automationexercise.com).

## Requirements

- Python 3.10+
- Google Chrome
- Google ChromeDriver
- `undetected-chromedriver`
- `pytest`
- `selenium`

## Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage

Run individual test files using:
```bash
pytest tests/test_register.py --browser=chrome
pytest tests/test_login.py --browser=chrome
pytest tests/test_delete_account.py --browser=chrome
```

All tests require Chrome to be installed.

Author
Guilherme Augusto dos Reis Martins