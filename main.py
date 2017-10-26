import os

import sendgrid
from flask import Flask, request, render_template
from sendgrid.helpers.mail import *

SENDGRID_API_KEY = "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"
app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def mail():
    if request.method == "POST":
        sg = sendgrid.SendGridAPIClient(apikey=SENDGRID_API_KEY)
        from_email = Email(request.form.get("from_email"))
        to_email = Email(request.form.get("to_email"))
        subject = request.form.get("subject")
        content = Content("text/plain", request.form.get("content"))
        mail = Mail(from_email, subject, to_email, content)
        
        try:
            response = sg.client.mail.send.post(request_body=mail.get())
            return render_template('success.html')
        except:
            return render_template('error.html', status_code="400")
    else:
        return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=True)
