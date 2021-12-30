import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

class EmailSender():

    def __init__(self, receiver_email, text = '', html= None):
        try:  
            self.sender_email = os.environ["EMAIL"]
            self.password = os.environ["PASSWORD"]
        except KeyError: 
            print("Please set the environment variable EMAIL")
            
        self.receiver_email = receiver_email
        self.text = text
        self.html = html
        self.status = 500
        self.send_email()

    def __str__(self):
        return str(self.status)

    def send_email(self):
        message = MIMEMultipart("alternative")
        message["Subject"] = "multipart test"
        message["From"] = self.sender_email
        message["To"] = self.receiver_email

        # Create the plain-text and HTML version of your message
        if not self.html:
            self.html = f"""\
                <html>
                    <body>
                    <p>Hello !, there is your token ! <br>
                        {self.text}
                        <a href="http://www.google.com"> This is just a Link Sample</a> 
                     </p>
                    </body>
                </html>
            """

        # Turn these into plain/html MIMEText objects
        part1 = MIMEText(self.text, "plain")
        part2 = MIMEText(self.html, "html")

        # Add HTML/plain-text parts to MIMEMultipart message
        # The email client will try to render the last part first
        message.attach(part1)
        message.attach(part2)

        # Create secure connection with server and send email
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            try:
                server.login(self.sender_email, self.password)
                server.sendmail(
                    self.sender_email, self.receiver_email, message.as_string()
                )
                self.status = 200
                print('------------ mandou o email ? ')
            except Exception as e:
                print(f"======================== {e}")