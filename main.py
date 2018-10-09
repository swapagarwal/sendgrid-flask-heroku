import os

import sendgrid
from flask import Flask, request
from sendgrid.helpers.mail import *

SENDGRID_API_KEY = os.environ.get("SENDGRID_API_KEY")

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
        response = sg.client.mail.send.post(request_body=mail.get())
        if response.status_code == 202:
            return "Email sent successfully!"
        else:
            return "Status Code: " + str(response.status_code)
    else:
        return """
        <html>
           <body>
              <form method = "POST">
                    <p><span style="
                        font-size: 1em;
                        font-family: sans-serif;
                        color: #3e4eb8;
                        border-left: 10px solid #3e4eb8;
                        padding: 10px;
                        margin: 10px 0;
                    ">From</span><input type="text" name="from_email" value="test@example.com" style="display: block;margin: 10px 0;border: 2px solid #3F51B5;padding: 10px;font-size: 1em;"></p>
                    <p><span style="
                        font-size: 1em;
                        font-family: sans-serif;
                        color: #3e4eb8;
                        border-left: 10px solid #3e4eb8;
                        padding: 10px;
                        margin: 10px 0;
                    ">To</span><input type="text" name="to_email" value="test@example.com" style="display: block;margin: 10px 0;border: 2px solid #3F51B5;padding: 10px;font-size: 1em;"></p>
                    <p><span style="
                        font-size: 1em;
                        font-family: sans-serif;
                        color: #3e4eb8;
                        border-left: 10px solid #3e4eb8;
                        padding: 10px;
                        margin: 10px 0;
                    ">Subject</span><input type="text" name="subject" value="Sending with SendGrid is Fun" style="display: block;margin: 10px 0;border: 2px solid #3F51B5;padding: 10px;font-size: 1em;width: 70%;"></p>
                    <p><span style="
                        font-size: 1em;
                        font-family: sans-serif;
                        color: #3e4eb8;
                        border-left: 10px solid #3e4eb8;
                        padding: 10px;
                        margin: 10px 0;
                    ">Message</span><input type="text" name="content" value="and easy to do anywhere, even with Python" style="display: block;margin: 10px 0;border: 2px solid #3F51B5;padding: 10px;font-size: 1em;width: 70%;">

                      <input type="submit" value="send email" style="
                        font-size: 1em;
                        border: none;
                        padding: 10px;
                        color: white;
                        background: #3d4abb;">

                    </p>
              </form>
           </body>
        </html>
        """


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=True)
