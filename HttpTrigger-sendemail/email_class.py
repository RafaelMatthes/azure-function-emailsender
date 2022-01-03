import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import logging
import os

class EmailSender():

    def __init__(self, receiver_email, text = '', link = None, html= None):
        try:  
            self.sender_email = os.environ["EMAIL"]
            self.password = os.environ["PASSWORD"]
        except KeyError: 
            print("Please set the environment variables")
            
        self.receiver_email = receiver_email
        self.text = text
        self.html = html
        self.link = link if link else 'https://google.com/404'
        self.status = 500
        self.send_email()

    def __str__(self):
        return str(self.status)

    def standard_html(self):
        return f"""\
                <html>
                    <body>
                    <p>Hello ! Thank you for your subscribe! <br>
                        {self.text}<br>
                        <a href="{self.link}"> Click here and confirm your e-mail</a> 
                     </p>
                    </body>
                </html>
            """
    
    def connection_smtp(self, message):
        """Create secure connection with server and send email"""
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                server.login(self.sender_email, self.password)
                server.sendmail(
                    self.sender_email, self.receiver_email, message.as_string()
                )
                self.status = 200
                logging.info('success')

    def send_email(self):
        message = MIMEMultipart("alternative")
        message["Subject"] = "Email Verification"
        message["From"] = self.sender_email
        message["To"] = self.receiver_email

        # Create the plain-text and HTML version of your message
        if not self.html:
            self.html = self.standard_html()

        # Turn these into plain/html MIMEText objects
        part1 = MIMEText(self.text, "plain")
        part2 = MIMEText(self.html, "html")

        # Add HTML/plain-text parts to MIMEMultipart message
        # The email client will try to render the last part first
        message.attach(part1)
        message.attach(part2)

        try:
            self.connection_smtp(message)
        except Exception as e:
            logging.error(f'{e}')
            print(f"error : {e}")