from email.header import decode_header
import email
import logging
import imaplib
import os
import time

logging.basicConfig(level=logging.INFO, datefmt="%Y-%m-%d", format="%(levelname)s - %(asctime)s - %(message)s")

class EmailClient:
    """
    Email Client 
    ------------
    Email Client for connecting to personal apple mail / icloud account. 
    Different methods and attributes will be used to iterate over mailboxes

    Methods:
    --------
        + test_connection
    """
    def __init__(self):
        self.__app_specific_password = os.getenv("APP_SPECIFIC_PASSWORD")  
        self.password = self.__app_specific_password  
        self.username = os.getenv("ICLOUD_EMAIL")
        self.mail = imaplib.IMAP4_SSL("imap.mail.me.com")

    def test_connection(self):
        """
        Test Connection 
        ---------------

        Using data passed from the parent class, test logging in to the email client 
        to ensure connection works. Then upon success, log out. 
        **Note: self.mail.close() only allowed in certain selected states

        Usage::

            >>> email_client = EmailClient()
            >>> email_client.test_connection()

        """
        try:
            self.mail.login(self.username, self.password)
            logging.info(f"Connection sucessful.")
            self.mail.logout()
            logging.info(f"Test completed.")
        except Exception as err: 
            logging.info(f"Houston we have a problem \n\n {err}")

