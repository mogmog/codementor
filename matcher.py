import models
from app import db
import os

class Matcher:

 def start(self):
    print(1)
    print (os.environ['DATABASE_URL'])
    result = models.Result(url="codementor.io")
    db.session.add(result)
    db.session.commit()
    return result.id

