from mongoengine import connect
import os
from loguru import logger
from dotenv import load_dotenv
load_dotenv()

db_string = os.getenv("MONGO_CONNECTION_STRING")
db_name = os.getenv("DB_NAME")

def db_connection():
    print(db_name,db_string)
    connect(db_name, host=db_string, port=27017)
    print("CONNECTION WITH DATABASE IS SUCCESSFUL")
    logger.info("Connected to MongoDB")
