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
            <!DOCTYPE html>
            <html>
            <head>
                <style>
                    * {
                      margin:0;
                      padding: 0;
                    }

                   
                    ::-webkit-input-placeholder { /* WebKit browsers */
                    font-family: 'Source Sans Pro', sans-serif;
                      color:    #fafafa;
                    font-weight: 300;
                  }
                  :-moz-placeholder { /* Mozilla Firefox 4 to 18 */
                    font-family: 'Source Sans Pro', sans-serif;
                     color:    #fafafa;
                     opacity:  1;
                    font-weight: 300;
                  }
                  ::-moz-placeholder { /* Mozilla Firefox 19+ */
                    font-family: 'Source Sans Pro', sans-serif;
                     color:    #fafafa;
                     opacity:  1;
                    font-weight: 300;
                  }
                  :-ms-input-placeholder { /* Internet Explorer 10+ */
                    font-family: 'Source Sans Pro', sans-serif;
                     color:    #fafafa;
                    font-weight: 300;
                  }
                    /*****
                      ========BUTTON========
                    *****/

                    .btn {
                      padding: 1em;
                      margin: 1em;
                      border: none;
                      border-radius: 3px;
                      color: rgba(0,0,0,.9);
                      outline: none;
                    }

                    .btn:hover {
                      cursor: pointer;
                      background: rgba(0,0,0,.4);
                      color: white;
                    }
                    /* inputs */
                    input:not([type]),
                    input[type=text],
                    input[type=password],
                    input[type=email],
                    input[type=url],
                    input[type=time],
                    input[type=date],
                    input[type=datetime],
                    input[type=datetime-local],
                    input[type=tel],
                    input[type=number],
                    input[type=search], textarea {
                      background-color: transparent;
                      outline: none;
                      border: 1px solid #bdbdbd;
                      border-radius: 5px;
                      width: 100%;
                      font-size: 16px;
                      padding: 12px 20px 12px 40px;
                      border: 1px solid #ddd;
                      margin-bottom: 12px;
                      transition: all 0.3s;
                      color: #fafafa;
                    }

                    body {
                      background: #14243d;
                      background: radial-gradient(ellipse at center, #14243d 0%, #030611 100%);
                    }

                    .btn {
                      background: #14243d;
                    }

                    .card {
                      margin:0 auto; margin-top: 3em; height: 300px; width: 40%; padding: 1em; text-align: center;
                    }

                    h1 {
                      font-weight:lighter; color: #fafafa; font-size: 3em; font-family: Castellar;
                    }
                    span.logo {
                      margin-top: -4em;
                    }

                  @media only screen
                  and (min-device-width: 320px)
                  and (max-device-width: 480px)
                  and (-webkit-min-device-pixel-ratio: 2)
                   {
                        ::-webkit-input-placeholder { /* WebKit browsers */
                    font-family: 'Source Sans Pro', sans-serif;
                      color:    #eee;
                    font-weight: 300;
                  }
                  :-moz-placeholder { /* Mozilla Firefox 4 to 18 */
                    font-family: 'Source Sans Pro', sans-serif;
                     color:    #eee;
                     opacity:  1;
                    font-weight: 300;
                  }
                  ::-moz-placeholder { /* Mozilla Firefox 19+ */
                    font-family: 'Source Sans Pro', sans-serif;
                     color:    #eee;
                     opacity:  1;
                    font-weight: 300;
                  }
                  :-ms-input-placeholder { /* Internet Explorer 10+ */
                    font-family: 'Source Sans Pro', sans-serif;
                     color:    #eee;
                    font-weight: 300;
                  }

                    span.logo {
                      font-size: 2em;
                      margin-left: 4em;
                      margin-top:-4.5em;
                    }
                    h1 {
                      font-size: 2em;
                      color: #fff;
                    }
                    .card {
                      width: 90%;
                      height: 490px;
                      margin-top: 3em;
                      background: none;
                      box-shadow: none;
                    }
                  
                    input[type="text"],input[type="email"],input[type="password"] {
                      /*padding: 1em;*/
                      font-size: 1em;
                      width: 100%;
                      color: #eee;
                    }

                    p {
                      font-size: 1em;
                      padding: 1em;
                      color: #eee;
                    }

                    .btn {
                      font-size: 1em;
                    }

                  }



                  @media only screen
                  and (min-device-width: 768px)
                  and (max-device-width: 1024px)
                  and (-webkit-min-device-pixel-ratio: 1)
                   {
                    ::-webkit-input-placeholder { /* WebKit browsers */
                    font-family: 'Source Sans Pro', sans-serif;
                      color:    #eee;
                    font-weight: 300;
                    }
                    :-moz-placeholder { /* Mozilla Firefox 4 to 18 */
                      font-family: 'Source Sans Pro', sans-serif;
                       color:    #eee;
                       opacity:  1;
                      font-weight: 300;
                    }
                    ::-moz-placeholder { /* Mozilla Firefox 19+ */
                      font-family: 'Source Sans Pro', sans-serif;
                       color:    #eee;
                       opacity:  1;
                      font-weight: 300;
                    }
                    :-ms-input-placeholder { /* Internet Explorer 10+ */
                      font-family: 'Source Sans Pro', sans-serif;
                       color:    #eee;
                      font-weight: 300;
                    }
                    span.logo {
                      margin-top:-4.5em;
                      margin-left: 1em;
                    }
                    h1 {
                      font-size: 2em;
                      color: #fff;
                    }
                    .card {
                      width: 90%;
                      height: 650px;
                      background: none;
                    }

                    input[type="text"],input[type="email"],input[type="password"] {
                      padding: 1em;
                      font-size: 1.3em;
                    }

                    p {
                      font-size: 2em;
                      padding: 1em;
                      color: #eee;
                    }

                    .btn {
                      font-size: 2em;
                    }
                  }
                </style>
                <title>SendGrid</title>
            </head>
            <body>
            <div class="card white shadow-2">
              <div class="contents">
                <h1>SendGrid</h1>
                <form method = "POST">
                      
                   <input type = "text" name = "from_email" placeholder="From" style="margin-top: 4em;" />
                   <input type = "text" name = "to_email" placeholder="To" />
                   <input type = "text" name = "subject" placeholder="Subject" />
                   <textarea name="content" placeholder="Your Contents here.." rows="10" ></textarea>
                   <input type = "submit" placeholder = "send email" class="btn" />
                </form>
              </div>
            </div>
            </body>
            </html>
        """


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=True)
