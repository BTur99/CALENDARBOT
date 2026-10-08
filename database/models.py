from .database import db
from peewee import Model, CharField, DateTimeField, TextField, BigIntegerField, IntegerField
import datetime

class BaseModel(Model):
    class Meta:
        database = db
        
class Users(BaseModel):
    username = CharField(null=True, unique=True)
    time_zone = IntegerField(null=True)
    tg_id = BigIntegerField(unique=True)
    created_at = DateTimeField(default=datetime.datetime.now)
    
def init_db():
    db.connect()
    db.create_tables([Users,])
    