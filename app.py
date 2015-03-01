from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from redis import Redis
from rq_scheduler import Scheduler
from datetime import datetime

import matcher
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


if __name__ == '__main__':
    app.run()

scheduler.schedule(
 scheduled_time=datetime.now(),
 func=matcher.Matcher().start,
 args=[],
 interval=60,
 repeat=10
)