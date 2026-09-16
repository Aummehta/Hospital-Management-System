from pymongo import AsyncMongoClient
from beanie import init_beanie
import os

async def init_db():
    # Retrieve the URI from environment or use default
    mongo_uri = os.environ.get("MONGO_URI", "mongodb://localhost:27017/doc")
    
    # Initialize native PyMongo async client
    client = AsyncMongoClient(mongo_uri)
    
    # Select the database
    db = client.get_database() # Defaults to 'doc' based on the URI, or you can specify client["doc"]
    
    return db
