import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.database import Base, engine
from app.routers import demo, admin

Base.metadata.create_all(bind=engine)

# Ensure app/static exists for StaticFiles mounting
os.makedirs("app/static", exist_ok=True)

app = FastAPI(title="2GIS Landing Generator & KP Outreach")

app.mount("/static", StaticFiles(directory="app/static"), name="static")

app.include_router(admin.router)
app.include_router(demo.router)
