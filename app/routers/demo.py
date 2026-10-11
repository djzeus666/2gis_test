from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Organization
from app.category_config import get_category_config

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

@router.get("/demo/{org_id}", response_class=HTMLResponse)
def render_demo_landing(org_id: str, request: Request, db: Session = Depends(get_db)):
    org = db.query(Organization).filter(Organization.id == org_id).first()
    if not org:
        raise HTTPException(status_code=404, detail="Organization not found")

    config = get_category_config(org.category)

    return templates.TemplateResponse(
        request=request,
        name="demo/landing.html",
        context={
            "org": org,
            "config": config
        }
    )
