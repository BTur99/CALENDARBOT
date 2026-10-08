from peewee import SqliteDatabase
import sqlite3
from config import Config

db = SqliteDatabase(Config.DB_NAME)

