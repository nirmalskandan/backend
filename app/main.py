from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pymongo import MongoClient
import os

# MongoDB connection
MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017/mydatabase")
client = MongoClient(MONGO_URL)
db = client.get_database()

app = FastAPI()

# Enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Update if needed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI"}

@app.get("/hello")
def health():
    return {"message": "Hello!"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/mongo-info")
def mongo_info():
    try:
        server_info = client.server_info()
        print(server_info)

        database_names = client.list_database_names()
        result = {
            "status": "connected",
            "host": client.HOST,
            "port": client.PORT,
            "server_version": server_info.get("version", "unknown"),
            "databases": [],
        }

        for db_name in database_names:
            database = client[db_name]
            result["databases"].append({
                "name": db_name,
                "collections": database.list_collection_names()
            })

        return result
    except Exception as e:
        return {"status": "error", "message": str(e)}
