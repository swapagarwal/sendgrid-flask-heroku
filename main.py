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
            <head>
              <title>Sendgrid Flask Heroku</title>
              <!-- bootstrap 4 sources for quick CSS -->
              <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-alpha.6/css/bootstrap.min.css" integrity="sha384-rwoIResjU2yc3z8GV/NPeZWAv56rSmLldC3R/AZzGRnGxQQKnKkoFVhFQhNUwEyJ" crossorigin="anonymous">
              <script src="https://code.jquery.com/jquery-3.1.1.slim.min.js" integrity="sha384-A7FZj7v+d/sdmMqp/nOQwliLvUsJfDHW+k9Omg/a/EheAdgtzNs3hpfag6Ed950n" crossorigin="anonymous"></script>
              <script src="https://cdnjs.cloudflare.com/ajax/libs/tether/1.4.0/js/tether.min.js" integrity="sha384-DztdAPBWPRXSA/3eYEEUWrWCy7G5KFbe8fFjk5JAIxUYHKkDx6Qin1DkWx51bBrb" crossorigin="anonymous"></script>
              <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-alpha.6/js/bootstrap.min.js" integrity="sha384-vBWWzlZJ8ea9aCX4pEW3rVHjgjt7zpkNpZk+02D9phzyeVkE+jo0ieGizqPLForn" crossorigin="anonymous"></script>
            </head>
            <body>
              <div class="container">

                <div class="page-header">
                  <h1>Sendgrid Flask Heroku</h1>
                </div>
                <hr>

                <form method = "POST" class="form-horizontal">
                  <div class="form-group row">
                    <label for="from_email" class="col-sm-2 col-form-label">From: </label>
                    <input type="text" name="from_email" placeholder="from@example.com" class="form-control col-sm-10" required/>
                  </div>

                  <div class="form-group row">
                    <label for="to_email" class="col-sm-2 col-form-label">To:</label>
                    <input type="text" name="to_email" placeholder="to@example.com" class="form-control col-sm-10" required>
                  </div>

                  <div class="form-group row">
                    <label for="subject" class="col-sm-2 col-form-label">Subject:</label>
                    <input type="text" name="subject" placeholder="Sending with SendGrid is Fun" class="form-control col-sm-10" required>
                  </div>

                  <div class="form-group row">
                    <label for="content" class="col-sm-2 col-form-label">Message:</label>
                    <textarea id="content" rows="5" placeholder="and easy to do anywhere, even with Python" class="form-control col-sm-10" required></textarea>
                  </div>

                  <div class="form-group row">
                    <div class="offset-sm-2 col-sm-10">
                      <button type="submit" class="btn btn-primary">Send Email</button>
                    </div>
                  </div>
                </form>
              </div>
            </body>
          </html>
        """


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=True)
