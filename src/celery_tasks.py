from celery import Celery
from asgiref.sync import async_to_sync
from typing import List
from src.mail import send_email




c_app=Celery()
c_app.config_from_object("src.config")

@c_app.task()
def send_email_tasks(self,recipients:List[str],subject:str,body:str):
    try:
        send_email(recipients, subject, body)
        return "Email sent successfully"
    except Exception as e:
        raise self.retry(exc=e, countdown=5)
    


