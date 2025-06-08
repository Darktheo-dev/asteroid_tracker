from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import requests
import os
from fastapi.responses import HTMLResponse
from fastapi.requests import Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

# Load environment variables from .env file
load_dotenv()

app = FastAPI()

# Serve static files (CSS, JS)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Serve HTML templates
templates = Jinja2Templates(directory="templates")

# Allow frontend JS to make requests to this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Get your NASA API key from the .env file
NASA_API_KEY = os.getenv("NASA_API_KEY")

# ============================
# Routes
# ============================

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/asteroids")
def get_asteroids():
    url = f"https://api.nasa.gov/neo/rest/v1/feed?api_key={NASA_API_KEY}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Failed to fetch asteroid data"}

@app.get("/asteroids-page", response_class=HTMLResponse)
def asteroids_page(request: Request):
    return templates.TemplateResponse("asteroids.html", {"request": request})

@app.get("/speed")
def calc_speed(distance_km: float, time_seconds: float):
    try:
        speed_km_per_sec = distance_km / time_seconds
        speed_m_per_sec = (distance_km * 1000) / time_seconds
        return {
            "distance_km": distance_km,
            "time_seconds": time_seconds,
            "speed_km_per_sec": speed_km_per_sec,
            "speed_m_per_sec": speed_m_per_sec
        }
    except Exception as e:
        return {"error": str(e)}

@app.get("/speed-page", response_class=HTMLResponse)
def speed_page(request: Request):
    return templates.TemplateResponse("speed.html", {"request": request})