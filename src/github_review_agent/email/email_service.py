import os
import resend
from  dotenv import load_dotenv
load_dotenv()

resend.api_key=os.getenv('RESEND_API_KEY')

class EmailService:
    def __init__(self):
        self.from_email=os.getenv('FROM_EMAIL')
    
    def send(
        self,
        to_email: str,
        subject: str,
        html: str,
        ):
        resend.Emails.send(
             {
                "from": self.from_email,
                "to": [to_email],
                "subject": subject,
                "html": html,
            }
        )
