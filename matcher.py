import models
from app import db
import os

class Matcher:

 def start(self):
    result = models.Result(url="working")
    db.session.add(result)
    db.session.commit()
    return result.id

