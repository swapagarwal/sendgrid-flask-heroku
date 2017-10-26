import os
import re

import sendgrid
from flask import Flask, request, render_template
from sendgrid.helpers.mail import *

SENDGRID_API_KEY = os.environ.get("SENDGRID_API_KEY")

app = Flask(__name__)

def checkSendGridKey(key):
    return re.match('^SG.[A-z0-9]{22}.[A-z0-9\-_]{43}$', key)

@app.route("/", methods=["POST", "GET"])
def mail():
    if request.method == "POST":
        if not checkSendGridKey(SENDGRID_API_KEY):
            return render_template('message.html', message="Status Code: 400", error=True)
        sg = sendgrid.SendGridAPIClient(apikey=SENDGRID_API_KEY)
        from_email = Email(request.form.get("from_email"))
        to_email = Email(request.form.get("to_email"))
        subject = request.form.get("subject")
        content = Content("text/plain", request.form.get("content"))
        mail = Mail(from_email, subject, to_email, content)
        response = sg.client.mail.send.post(request_body=mail.get())
        if response.status_code == 202:
            return render_template('message.html', message="Email sent successfully!", error=False)
        else:
            return render_template('message.html', message="Status Code: " + str(response.status_code), error=True)
    else:
        return render_template('email-form.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=True)
