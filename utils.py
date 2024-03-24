from pathlib import Path
from email.message import EmailMessage
import smtplib
import ssl
from streamlit import st

current_folder = Path(__file__).parent
templates_folder = current_folder / 'templates'
email_list_folder = current_folder / 'email_list'
settings_folder = current_folder / 'settings'

def init():
  if not 'email_manager_page' in st.session_state:
    st.session_state.email_manager_page = 'home'
  if not 'current_addressees' in st.session_state:
    st.session_state.current_addressees = ''
  if not 'current_title' in st.session_state:
    st.session_state.current_title = ''
  if not 'current_body' in st.session_state:
    st.session_state.current_body = ''

def change_page(page_name):
  st.session_state.email_manager_page = page_name

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
  
