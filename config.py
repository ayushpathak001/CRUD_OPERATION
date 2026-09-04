from dotenv import load_dotenv
import os 
import motor.motor_asyncio
load_dotenv()
0

MONGO_URI = os.getenv("MONGO_URI" , "")
DB_NAME = os.getenv("DB_NAME" , "")


client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URI)
mongo_db = client[DB_NAME]




