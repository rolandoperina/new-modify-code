# Internet Connection Checker

## Project Overview

The **Internet Connection Checker** is a Python script designed to test the availability of an internet connection by attempting to connect to a specified URL. The script provides feedback on the connection status and allows users to input different URLs for testing. It implements defensive programming techniques to ensure robustness and reliability.

### Rationale for Choosing This Project

This project was chosen to demonstrate basic network connectivity testing using Python. It serves as a practical example of how to handle HTTP requests, implement error handling, and enhance user interaction in a command-line application.

## Installation and Setup Guide

### Prerequisites

- Python 3.x installed on your machine.
- The `requests` library, which can be installed via pip.

### Steps to Set Up the Development Environment

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/YOUR_USERNAME/YOUR_FORKED_REPO.git
   cd YOUR_FORKED_REPO
   Install Dependencies: Install the required libraries using pip:
bash

Verify

Open In Editor
Run
Copy code
pip install requests
Usage
Run the Script: Execute the script using the command line:

bash

Verify

Open In Editor
Run
Copy code
python new_modify_project.py
Input a URL: When prompted, enter a URL to test. If you press Enter without typing anything, the default URL (https://www.google.com/) will be used.

View Results: The script will display whether the connection to the specified URL was successful or if there were any errors.

Retry: After each test, you will be asked if you want to test another URL. Type "yes" to continue or "no" to exit the program.

Features
URL Validation: Ensures that the provided URL is in a valid format before attempting to connect.
Detailed Error Messages: Provides specific feedback for connection failures, timeouts, and other exceptions.
User Interaction: Allows users to input multiple URLs in a single session for testing.
Defensive Programming Techniques
The script implements several defensive programming techniques, including:

Input Validation: Validates the format of the URL before making a request.
Error Handling: Catches specific exceptions and provides meaningful feedback to the user.
User Feedback: Displays clear messages to inform the user of the connection status.
Testing
The script has been tested with various scenarios, including:

Valid URLs (e.g., https://www.google.com/)
Invalid URLs (e.g., htp://invalid-url)
URLs that are unreachable (e.g., https://www.nonexistentwebsite.com/)
License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
Thanks to the Python community for their extensive documentation and resources.
Special thanks to the developers of the requests library for making HTTP requests easy in Python.
