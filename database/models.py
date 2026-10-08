from .database import db
from peewee import Model, CharField, DateTimeField, BigIntegerField
import datetime

class BaseModel(Model):
    class Meta:
        database = db
        
class User(BaseModel):
    username = CharField(null=True)
    time_zone = CharField(null=True)
    tg_id = BigIntegerField(unique=True)
    created_at = DateTimeField(default=datetime.datetime.now)
    
def init_db():
    db.connect()
    db.create_tables([User,])
    