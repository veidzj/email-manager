from email.message import EmailMessage
import smtplib
import ssl

def send_email(user_email, addressees, title, body, app_password):
  email_message = EmailMessage()
  email_message['From'] = user_email
  email_message['To'] = addressees
  email_message['Subject'] = title

  email_message.set_content(body)
  safe = ssl.create_default_context()

  with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=safe) as smtp:
    smtp.login(user_email, app_password)
    smtp.sendmail(user_email, addressees, email_message.as_string())
  
