import smtplib
import ssl
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(sender_email, receiver_email, subject, body, smtp_server, smtp_port, login, password):
    # Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    
    # Add body to email
    message.attach(MIMEText(body, "plain"))
    
    try:
        # Connect to the SMTP server and send email using TLS
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.ehlo()  # Can be omitted
            server.starttls()  # Secure the connection
            server.ehlo()  # Can be omitted
            server.login(login, password)
            server.sendmail(sender_email, receiver_email, message.as_string())
            print("Email sent successfully!")
    except smtplib.SMTPRecipientsRefused:
        print(f"Error: The recipient email address '{receiver_email}' does not exist.")
    except smtplib.SMTPAuthenticationError:
        print("Error: Authentication failed. Please check your login credentials.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Usage example
creds = os.getenv("APP_SPECIFIC_PASSWORD") 
sender_email = "info@teraearlywine.com"
receiver_email = "dev@teraearlywine.com"
subject = "Test Email"
body = "This is a test email sent from a Python script."
smtp_server = "smtp.mail.me.com"  # Apple's iCloud SMTP server
smtp_port = 587  # SSL port for SMTP
login = os.getenv("ICLOUD_EMAIL")  # Your email login (Apple ID email)
password = creds # Your email password (consider using app-specific password)

send_email(sender_email, receiver_email, subject, body, smtp_server, smtp_port, login, password)