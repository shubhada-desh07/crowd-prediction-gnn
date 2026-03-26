from fastapi import FastAPI
from main import main

app = FastAPI()

@app.get("/crowd_status")
def get_status():
    result = main()
    return result