import smtplib
import ssl
import csv
import getpass
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = input("Your email: ")
password = getpass.getpass("Type your password and press enter:")
input("Save the target emails into target_emails.csv, press enter to continue...")

receiver_emails = []
links = []
first_names = []
with open('target_emails.csv', 'r') as f:
    csv_reader = csv.reader(f)

    for row in csv_reader:
        receiver_emails.append(row[0])
        first_name = row[1].split(" ")[0]
        first_names.append(first_name)
        links.append(row[2])

# Create secure connection with server and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    print("Starting server")
    server.login(sender_email, password)
    print("Logged in")
    for i in range(len(receiver_emails)):
        message = MIMEMultipart("alternative")
        message["Subject"] = "STC WordPress Workshop | Generated Wpsandbox Link"
        message["From"] = sender_email
        message["To"] = receiver_emails[i]

        # Create the plain-text and HTML version of your message
        text = f"""\
    Hi {first_names[i]},
    This is your generated wpsanbox link, it will be used in our hands-on session: 
    {links[i]}

    Link is generated from https://wpsandbox.net/ if you would like to generate your own sandbox in future (It will be blocked by School/University network), you may check out their website!

    If you have any questions/difficulties, please do not hesitate to email/message us!

    *Please have your dinner before the event, and do bring along your jacket as the venue might be cold!

    See you there!

    Chai,
    Committee of Sunway Tech Club
    """

        html = f"""\
    <html>
      <body>
        <p>Hi {first_names[i]},
          <br>
          <br>
          This is your generated wpsanbox link, it will be used in our hands-on session: 
          <br>
          <a href="{links[i]}">{links[i]}</a> 
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

        # Turn these into plain/html MIMEText objects
        part1 = MIMEText(text, "plain")
        part2 = MIMEText(html, "html")

        # Add HTML/plain-text parts to MIMEMultipart message
        # The email client will try to render the last part first
        message.attach(part1)
        message.attach(part2)

        print(f"Sending to: {receiver_emails[i]}")
        server.sendmail(
            sender_email, receiver_emails[i], message.as_string()
        )
print("Done")
