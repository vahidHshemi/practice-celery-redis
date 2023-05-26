import time
from django.shortcuts import render
from django.http import HttpResponse
from core.celery import app
from .tasks import my_task_2

# Create your views here.
@app.task
def my_task():
    time.sleep(10)
    open('test2.txt', 'w').close()

def home(request):
    
    my_task.delay()
    my_task_2.delay()
    
    return HttpResponse('Hello and welcome to my celery course!')
