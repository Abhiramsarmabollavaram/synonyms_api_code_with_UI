from fastapi import FastAPI, Form
from pydantic import BaseModel
import json
import pdb

app = FastAPI()
JSON_FILE_PATH = r"C:\Users\E010649\Desktop\final_synonyms_api\synonyms.json"
@app.get("/get-dictionary/")
def load_existing_json():
    try:
        with open(JSON_FILE_PATH, "r") as file:
            pdb.set_trace()
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}  # Return an empty dictionary if file doesn't exist or is invalid


