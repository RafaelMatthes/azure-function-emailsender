import logging
import azure.functions as func
from .email_class import EmailSender

def main(req: func.HttpRequest) -> func.HttpResponse:
    receiver = req.params.get('receiver_email')
    text = req.params.get('aditional_text','')
    link = req.params.get('link', None)
    html = req.params.get('html_text', None)

    if receiver:
        this_email = EmailSender(receiver, link=link, text= text, html=html)
        return func.HttpResponse('', status_code=this_email)
    else:
        logging.error(f'Request without receiver email')
        return func.HttpResponse(
            "",
            status_code=100
        )
