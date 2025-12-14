import json
from django.core.mail import send_mail
from django.core.files import File
import datetime


def send(user_email):
    send_mail(
        subject='надсилаю на майл',
        message='спам1',
        from_email='bkuzik14@gmail.com',
        recipient_list=[user_email],
        fail_silenty=False,
    )
    # f = open(f'./emails.txt', 'a')
    # testfile = File(f)
    # testfile.write(str(datetime.datetime.now()) + "  " + user_email + '\n')
    # testfile.close()
    # f.close()


def save_categories(data):
    with open(f'./categories.json', 'a') as file:
        json.dump(data, file)
