import sqlite3
from peewee import SqliteDatabase
from config import Config

db = SqliteDatabase(Config.DB_NAME)

