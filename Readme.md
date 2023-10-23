# Selenium Python Framework

## Table of Contents

- [Introduction](#Introduction)
- [Key Features](#key-features)
- [Usage](#usage)
- [Folder Structure](#folder-structure)
- [Running Tests](#running-tests)
- [Contributing](#contributing)
- [Contact](#Contact)

## Introduction

The *Selenium Python Framework* is a comprehensive Python-based Automated Web Testing Framework designed to streamline and automate web testing processes. It offers a set of powerful and generic methods to interact with web elements, handle common browser actions, and execute test cases efficiently. This framework aims to simplify web testing for both manual testers and automation engineers, ensuring faster test execution, improved reliability, and enhanced test coverage.

### Key Features

- **Generic Methods:** The framework provides a collection of generic methods for interacting with web elements, such as clicking, entering text, and checking element presence. These methods are reusable across different test scenarios, reducing code duplication and enhancing maintainability.

- **Global Wait Time:** The framework incorporates a global wait time setting, ensuring that the system waits for the specified duration before timing out when searching for elements. This improves stability and robustness when dealing with dynamic web pages.

- **Screenshot Capture :** With built-in screenshot capture functionality, the framework allows users to generate screenshots for failed test cases, aiding in debugging and troubleshooting.

- **Browser Configuration:** The framework supports multiple browsers, such as Chrome, Firefox, Internet Explorer, and Edge. Users can easily configure the desired browser for test execution.

- **Page Object Model (POM) Pattern:** The framework follows the Page Object Model pattern to organize and maintain web page elements and their corresponding actions in separate classes, promoting code clarity and reusability.

## Usage

1. **Test Case Definition:** Define test cases using Python and utilize the provided generic methods to interact with web elements. Users can create test classes that inherit from the `BaseTest` class, which already includes the required fixture for initializing the browser.

2. **Web Page Mapping:** Create page classes representing web pages in the application under test. These page classes should extend the `GenericMethods` class to inherit its generic methods.

3. **Running Tests:** Execute test cases using the test runner of your choice, such as Pytest. The framework will handle browser setup and teardown automatically for each test class.

## Folder Structure

- **`Pages/`:** Contains page classes representing web pages in the application.
- **`KeywordLibrary/`:** Contains the `GenericMethods` class with reusable generic methods.
- **`Tests/`:** Contains test classes defining test scenarios.
- **`Config/`:** Contains configuration files for setting global variables and preferences.
- **`Reports/`:** Contains reports integrated with allure report (Make sure to add argument in config so that it gets generated in Report folder "-v -n 1 --alluredir=../Reports/jsonreports").
- **`TestData/`:** Contains test data which makes the framework data driven.

## Running Tests

1. Install the required Python packages and dependencies (pip install -r requirements.txt).
2. Configure the test environment and browser preferences in the `config_data.py` file.
3. Run test classes using your preferred test runner (Pytest).

## Contributing

We welcome contributions to this framework. If you encounter any issues, have ideas for improvements, or want to add new features, please follow the contribution guidelines provided in the project's repository.

## Contact

For any questions or support related to the project, feel free to contact Harshit Sinha at hsinha22@gmail.com.
