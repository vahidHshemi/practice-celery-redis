from __future__ import with_statement
from ast import With
from celery import shared_task
from core.celery import app

@app.task
def my_task_2():
    with open('test3.txt', 'a') as file:
        file.write('Hello world! ')