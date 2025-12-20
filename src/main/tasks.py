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

@app.task()
def my_sum(a, b):
    return a + b

@app.task(bind=True, default_retry_delay= 5 * 60)
def task_retry(self, x, y):
    try:
        return x + y
    except Exception as exc:
        raise self.retry(exc=exc, countdown=60)