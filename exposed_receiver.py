from fastapi import FastAPI
import requests
import json
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
import pdb
app = FastAPI()


JSON_FILE_PATH = r"C:\Users\E010649\Desktop\final_synonyms_api\synonyms.json"
app.mount("/static", StaticFiles(directory=r"C:\Users\E010649\Desktop\Finale\static"), name="static")


def load_existing_json():
    try:
        with open(JSON_FILE_PATH, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_updated_json(data):
    with open(JSON_FILE_PATH, "w") as file:
        json.dump(data, file, indent=4)

@app.post("/update-synonyms/")
async def update_synonyms(request: Request):
    existing_json = load_existing_json()
    submitted_data = await request.json()
        
    for key, value in submitted_data.items():
        if key in existing_json:
            if value not in existing_json[key]:
                existing_json[key].append(value)
        else:
            
            existing_json[key] = [value]

    save_updated_json(existing_json)

    return {"message": "Synonyms updated successfully", "updated_data": existing_json}


templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    existing_json = load_existing_json()
    max_values = max(len(values) for values in existing_json.values())
    return templates.TemplateResponse("index.html", {"request": request, "data":existing_json, "max_values": max_values})