from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from redis import Redis
from rq_scheduler import Scheduler
from datetime import datetime
from service import do_something_with_database
import os
from datetime import datetime, timedelta

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
db = SQLAlchemy(app)

scheduler = Scheduler(connection=Redis()) # Get a scheduler for the "default" queue

if __name__ == '__main__':
    scheduler.enqueue_at(datetime.now() + timedelta(seconds=5) , do_something_with_database)
    #app.run()

