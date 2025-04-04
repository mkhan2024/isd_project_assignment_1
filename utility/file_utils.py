__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = "Md Apurba Khan"

import os

def simulate_send_email(email_address, subject, message):
    """Simulate sending an email by writing to a file."""
    directory = "output"
    filename = "observer_emails.txt"
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    path = os.path.join(project_root, directory, filename)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "a") as file:
        file.write(f"---\nTo: {email_address}\nSubject: {subject}\nMessage: {message}\n---\n")