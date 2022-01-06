# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 10:58:27 2022

@author: User
"""

from flask import Flask
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from flask import request

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/correo")
def enviarCorreo():
    destino = request.args.get("destino")
    asunto  = request.args.get("asunto")
    mensaje = request.args.get("mensaje")
    hashString = request.args.get("hash")
    if(hashString == os.environ.get("SECURITY_HASH")):
        message = Mail(
            from_email=os.environ.get("from_email"),
            to_emails = destino,
            subject = asunto,
            html_content= mensaje )
        try:
            sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
            response = sg.send(message)
            print("Enviado")
            return "OK"
        except Exception as e:
            print(e.message)
            return "KO"
    else:
        print("Hash error")
        return "KO"

if __name__ == "__main__":
    app.run()
    
   