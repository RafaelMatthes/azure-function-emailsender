from email.mime import text
import logging
import azure.functions as func
from .email_class import EmailSender
import json

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    receiver = req.params.get('destino')
    text = req.params.get('texto')

    # if not receiver or not text:
    #     try:
    #         req_body = req.get_json()
    #     except ValueError:
    #         pass
    #     else:
    #         receiver = req.params.get('destino')
    #         text = req.params.get('texto')

    if receiver:
        this_email = EmailSender(receiver, text= text)
        return func.HttpResponse('foooi', status_code=this_email)
    else:
        return func.HttpResponse(
            "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
            status_code=200
        )
