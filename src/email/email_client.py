
import logging
import imaplib
import os
import email
from email.header import decode_header

logging.basicConfig(level=logging.INFO, datefmt="%Y-%m-%d", format="%(levelname)s - %(asctime)s - %(message)s")

class EmailClient:
    """
    Email Client 
    ------------
    Email Client for connecting to personal apple mail / icloud account. 
    Different methods and attributes will be used to iterate over mailboxes

    Attributes: 
    -----------
    The following private attributes are passed as data in order to login to the icloud email app. 
    The last 'mail' attribute is the official server connection string, and is repeatedly referenced
    in the other methods. i.e. `self.mail.login(self._username, self._password)`. This is for security
    purposes, to login and close the connection in each method.

    `_password: STR` 
        Definition: apple provided app specific password
    `_username: STR` 
        Definition: full iCloud email account
    `mail: OBJ` 
        Definition: mail server access string via imaplib.IMAP4_SSL

    Methods:
    --------
        `test_connection: BOOL`
            Definition: tests loging into email account. Returns True if successful, False if unsuccessful
    """
    def __init__(self):
        self._app_specific_password = os.getenv("APP_SPECIFIC_PASSWORD")  
        self._password = self._app_specific_password  
        self._username = os.getenv("ICLOUD_EMAIL")
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
            self.mail.login(self._username, self._password)
            logging.info(f"Connection sucessful.")
            self.mail.logout()
            return True
        except Exception as err: 
            logging.info(f"Houston we have a problem \n\n {err}")
            return False

    def get_mailboxes(self):
        """
        Get Mailboxes
        -------------

        Get all available mailbox names in a user-friendly format.
        
        Note: `mail.list()` returns a tuple containing status and list of mailboxes that are in bytes, 
        unpack and convert to string datatype. Each mailbox is also a tuple datatype, unpack these as well to access the mailbox name.
        
        Returns:
            data type: `list`
                A list of available mailbox names.

        ----

        Usage::

            >>> email_client = EmailClient()
            >>> mailboxes = email_client.get_mailboxes()
            >>> print(mailboxes)

        """

        self.mail.login(self._username, self._password)
        _, mailboxes  = self.mail.list()

        available_mailboxes = []
        for mailbox in mailboxes: 
           flags, _, mailbox_name = mailbox.decode().split('"', 2)
           mailbox_name = mailbox_name.replace('"', ' ').strip() 
           available_mailboxes.append(mailbox_name)
        self.mail.logout()
        logging.info(f"{len(available_mailboxes)} available mailboxes")
        return available_mailboxes

# TODO: Add SMTP email processing
# TODO: Refactor SMTP to be more user friendly / maintainable