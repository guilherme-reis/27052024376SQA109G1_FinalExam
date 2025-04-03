
# SQA109 Final Exam - Automation Testing with Selenium


### Website URL:
- https://www.automationexercise.com/

### Use Cases:
1. **User Registration:**
   - Automate the process of a new user registering on the website by filling out the sign-up form with random user data.
   
2. **Login Functionality:**
   - Automate the login process using valid credentials, verify that the user can successfully log in, and ensure the user is redirected to the homepage.
   
3. **Account Deletion:**
   - Automate the account deletion process by logging in with valid credentials and confirming that the user can successfully delete their account.

4. **Navigating to Product Page:**
   - Automate navigation to the product page, select a product, and ensure that the correct product details are displayed.

5. **Logout Functionality:**
   - Automate the logout process after the user logs in, ensuring the user is logged out successfully and redirected to the homepage.

### Locator Strategies:
- **User Registration:**
  - Use `By.NAME`, `By.XPATH`, and `By.ID` to locate form fields and buttons such as "signup-email", "password", "name", and "create-account".
  
- **Login Functionality:**
  - Use `By.NAME` to locate the email and password fields, and `By.XPATH` or `By.CLASS_NAME` to find the login button.
  
- **Account Deletion:**
  - Use `By.XPATH` to locate the delete account button after login, and use `By.ID` to confirm the account is deleted.
  
- **Product Page Navigation:**
  - Use `By.LINK_TEXT` or `By.XPATH` to locate and click product links, and `By.CSS_SELECTOR` to ensure product details are loaded.

- **Logout Functionality:**
  - Use `By.LINK_TEXT` to locate the logout button and `By.XPATH` to confirm the user is redirected after logging out.

### Browser Compatibility:
- **Google Chrome (Chromium)**
- **Safari (WebKit)**

## Overview

This project implements end-to-end automation testing for the **Automation Exercise** website. The tests cover three core functionalities:
1. **User Registration**
2. **User Login**
3. **Account Deletion**

The tests are written in Python using **Selenium WebDriver** and **Pytest** for cross-browser testing on **Chrome** and **Safari**.

## Technologies Used

- **Python 3.x**
- **Selenium WebDriver**
  - Used for web automation across different browsers.
  - **undetected_chromedriver** for Chrome automation.
- **Pytest**
  - For running the tests and assertions.
- **WebDriverWait & ExpectedConditions**
  - For handling dynamic page elements and ensuring synchronization during tests.

## Project Structure

```
automationexercise-final/
├── tests/
│   ├── test_register.py          # User registration test
│   ├── test_login.py             # User login test
│   └── test_delete_account.py    # Account deletion test
├── venv/                         # Virtual environment for dependencies
├── README.md                     # Project description
└── .gitignore                    # Git ignore file for unnecessary files
```

## Prerequisites

To run this project, you will need:

- Python 3.x installed on your system.
- **Selenium WebDriver** and **Pytest** installed in your Python environment.
- A **Chrome** or **Safari** browser for testing.

## Setup and Installation

### 1. **Clone the Repository**
Start by cloning the repository to your local machine:
```bash
git clone https://github.com/guilherme-reis/27052024376SQA109G1_FinalExam.git
cd 27052024376SQA109G1_FinalExam/automationexercise-final
```

### 2. **Create a Virtual Environment**
Create a virtual environment for the project:
```bash
python3 -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scriptsctivate     # On Windows
```

### 3. **Install Dependencies**
Install all required Python dependencies using **pip**:
```bash
pip install -r requirements.txt
```

If the `requirements.txt` is missing or you need to manually install:
```bash
pip install selenium pytest undetected-chromedriver
```

## Running the Tests

To run the tests in both browsers, use the following commands:

### 1. **Running Tests in Chrome**
```bash
pytest tests/test_register.py --browser=chrome
pytest tests/test_login.py --browser=chrome
pytest tests/test_delete_account.py --browser=chrome
```

### 2. **Running Tests in Safari**
```bash
pytest tests/test_register.py --browser=safari
pytest tests/test_login.py --browser=safari
pytest tests/test_delete_account.py --browser=safari
```

This will execute the tests in both **Chrome** and **Safari**, depending on which browser you specify.

## How the Tests Work

### 1. User Registration
- Navigate to the **Signup/Login** page.
- Fill in the registration form with random details (using random email generation).
- Verify the "Account Created!" message to confirm successful registration.

### 2. User Login
- Log in with the newly created user.
- Verify the "Logged in as" message to ensure the user is logged in.

### 3. Account Deletion
- Delete the user account after login.
- Ensure that the user can no longer log in after account deletion.

## Error Handling

- **Element Not Clickable**: If an element is not clickable, the script uses JavaScript execution to click the element as a fallback.
- **Dynamic Content Handling**: `WebDriverWait` is used to wait for elements to become visible or clickable, ensuring synchronization between the tests and the web page.

## Screenshots

During test failures, screenshots are automatically saved to the working directory for debugging.
