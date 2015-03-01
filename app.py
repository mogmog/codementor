from flask import Flask, render_template, request, jsonify
from flask.ext.sqlalchemy import SQLAlchemy
from collections import Counter
from rq import Queue
from rq.job import Job
from worker import conn
import operator
import os
import re
import json
import os
from datetime import datetime

import redis
from rq import Worker, Queue, Connection
from redis import Redis
from rq_scheduler import Scheduler


listen = ['default']

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
db = SQLAlchemy(app)

q = Queue(connection=conn)

import models
import matcher

redis_url = os.getenv('REDISTOGO_URL', 'redis://localhost:6379')

conn = redis.from_url(redis_url)

if __name__ == '__main__':

 scheduler = Scheduler(connection=Redis()) # Get a scheduler for the "default" queue

 dt = datetime(2015, 3, 1, 19, 46)

 scheduler.schedule(
     scheduled_time=datetime.now(), # Time for first execution, in UTC timezone
     func=matcher.Matcher().start,                     # Function to be queued
     args=[],             # Arguments passed into function when executed
     interval=60,                   # Time before the function is called again, in seconds
     repeat=5                      # Repeat this number of times (None means repeat forever)
 )

 print (len(scheduler.get_jobs()))



