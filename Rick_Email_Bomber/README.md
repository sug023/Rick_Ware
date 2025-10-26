# README for EmailBomber

## Description

`EmailBomber` is a Python script designed to send a large number of emails to a specified target email address. It uses multiple email accounts and can customize the content of each email. This script is useful for stress-testing email servers or for sending mass emails for various purposes.

## Features

- **Multiple Email Accounts**: Supports the use of multiple email accounts for sending emails.
- **Custom Email Content**: Allows customization of email subjects and messages from a JSON file.
- **Delay Between Emails**: Option to set a delay between sending each email.
- **Retry Mechanism**: Implements a retry mechanism in case of temporary failures.
- **Email Validation**: Validates email formats to ensure correctness.

## Requirements

- Python 3.x
- Additional libraries: `smtplib`, `email.mime.text`, `email.mime.multipart`, `os`, `json`, `re`, `pathlib`, `sys`, `time`

## Installation

1. Ensure you have Python 3.x installed on your system.
2. No additional installations are required as the script uses standard Python libraries.

## Usage

### Example Usage

```python
es = EmailBomber()
es.run()
````

### Parameters

- **`bots.txt`**: A file containing email credentials in the format `email/app_password`. Each line should contain one set of credentials.
- **`content.json`**: A JSON file containing email subjects and messages. The format should be a dictionary where keys are subjects and values are message bodies.

### Running the Script

1. Prepare the `bots.txt` file with your email credentials.
2. Prepare the `content.json` file with the email content.
3. Run the script:
    
    bash
    

4. ```bash
    python email_bomber.py
    ```
    
5. Follow the prompts to enter the target email, file paths, and delay between emails.

## Internal Workings

### Class `EmailBomber`

- **`__init__`**: Initializes the instance with default paths and settings.
- **`find_file`**: Searches for a file in the current working directory or the script directory.
- **`read_credentials`**: Reads email credentials from `bots.txt` and validates them.
- **`read_content`**: Reads email content from `content.json` and validates the JSON format.
- **`bomb_email`**: Sends emails using the provided server and credentials. Implements a retry mechanism for temporary failures.
- **`get_script_dir`**: Determines the directory of the script, useful for finding resources.
- **`spam_email`**: Orchestrates the reading of credentials and content, then sends the emails.
- **`check_email`**: Validates the format of an email address using a regular expression.
- **`validate_file`**: Checks if a file exists and has the correct extension.
- **`run`**: Main method to execute the script, handling user input and starting the email bombing process.

## Notes

- This script is designed to work with Gmail's SMTP server. Ensure that the email accounts used have "Less secure app access" enabled or use app-specific passwords.
- The script clears the screen before prompting for user input to keep the interface clean.
- The delay between emails can be adjusted to avoid rate limiting by email servers.

# DISCLAIMER:
This script is provided for educational and research purposes only. The author assumes no responsibility for any misuse, damage, or illegal activity caused by the use of this code. Use it at your own risk and ensure compliance with all applicable laws and regulations.
