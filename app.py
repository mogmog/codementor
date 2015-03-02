from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from redis import Redis
from rq_scheduler import Scheduler
from datetime import datetime

import os

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
db = SQLAlchemy(app)

scheduler = Scheduler(connection=Redis()) # Get a scheduler for the "default" queue

@app.route('/')
def hello():
    return "Hello World!"


@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)

def matcherrr():
     print(55)
     return 1

if __name__ == '__main__':

    list_of_job_instances = scheduler.get_jobs()

    print (list_of_job_instances)
    for job in list_of_job_instances:
     scheduler.cancel(job)

    scheduler.schedule(
     scheduled_time=datetime.now(),
     func= matcherrr,
     args=[],
     interval=60,
     repeat=10
    )

    app.run()

