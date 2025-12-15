import requests
from celery import shared_task
from proj.celery import app
from src.main.service import send
import time 
from django.core.mail import send_mail

@app.task()
def send_spam_email(user_email, text):
    send(user_email = user_email, text=text)
    return f"True +{user_email}"
