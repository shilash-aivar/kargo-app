from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import os

app = FastAPI()

APP_VERSION = os.getenv("APP_VERSION", "dev")
APP_ENV = os.getenv("APP_ENV", "dev")
APP_COLOR = {
    "dev": "#4f86f7",
    "staging": "#f7a134",
    "prod": "#3cb371",
}.get(APP_ENV, "#888")


@app.get("/", response_class=HTMLResponse)
def index():
    return f"""
    <html>
      <body style="font-family:sans-serif;display:flex;align-items:center;justify-content:center;height:100vh;margin:0;background:{APP_COLOR}20">
        <div style="text-align:center;padding:3rem;border-radius:1rem;background:{APP_COLOR};color:#fff;box-shadow:0 4px 20px rgba(0,0,0,.2)">
          <h1 style="margin:0;font-size:3rem">Kargo Demo App</h1>
          <p style="font-size:1.5rem;margin:.5rem 0">Environment: <strong>{APP_ENV.upper()}</strong></p>
          <p style="font-size:1.2rem;margin:.5rem 0">Version: <strong>{APP_VERSION}</strong></p>
        </div>
      </body>
    </html>
    """


@app.get("/healthz")
def healthz():
    return {"status": "ok", "env": APP_ENV, "version": APP_VERSION}


@app.get("/info")
def info():
    return {"env": APP_ENV, "version": APP_VERSION}
