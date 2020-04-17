import smtplib
import ssl
import csv
import getpass
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = input("Your email: ")
password = getpass.getpass("Type your password and press enter:")
input("Save the target emails into target_emails.csv, press enter to continue...")

receiver_email = ""
first_name = ""

subject = ""
text = f"""\
    Hi {first_name},
    Chai,
    Committee of Sunway Tech Club
    """
html = f"""\
    <html>
      <body>
        <p>Hi {first_name},
          <br>
          <br>
          This is your generated wpsanbox link, it will be used in our hands-on session: 
          <br>
          <br>
          Link is generated from <a href="https://wpsandbox.net/">wpsandbox.net</a>, if you would like to generate your own sandbox in future (It will be blocked by School/University network), you may check out their website!
          <br>
          <br>
          If you have any questions/difficulties, please do not hesitate to email/message us!
          <br>
          <br>
          *Please have your dinner before the event, and do bring along your jacket as the venue might be cold!
          <br>
          <br>
          See you there!
          <br>
          <br>
          <br>
          Chai,
          <br>
          Committee of Sunway Tech Club
        </p>
      </body>
    </html>
    """

# Create secure connection with server and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    print("Starting server")
    server.login(sender_email, password)
    print("Logged in")
    message = MIMEMultipart("alternative")
    message["Subject"] = subject
    message["From"] = sender_email
    message["To"] = receiver_email

    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)
    message.attach(part2)

    print(f"Sending to: {receiver_email}")
    server.sendmail(
        sender_email, receiver_email, message.as_string()
    )
print("Done")
