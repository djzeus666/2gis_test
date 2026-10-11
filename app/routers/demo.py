from typing import Optional
from fastapi import APIRouter, Depends, HTTPException, Request, Query
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Organization
from app.category_config import get_category_config, get_template_config, TEMPLATES_CONFIG

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

@router.get("/demo/{org_id}", response_class=HTMLResponse)
def render_demo_landing(
    org_id: str,
    request: Request,
    template: Optional[int] = Query(None, description="Template ID from 1 to 10"),
    db: Session = Depends(get_db)
):
    org = db.query(Organization).filter(Organization.id == org_id).first()
    if not org:
        raise HTTPException(status_code=404, detail="Organization not found")

    config = get_category_config(org.category)

    # Determine selected template ID (fallback to category default or template 1)
    template_id = template if (template and template in TEMPLATES_CONFIG) else config.get("default_template_id", 1)
    template_cfg = get_template_config(template_id)

    return templates.TemplateResponse(
        request=request,
        name="demo/landing.html",
        context={
            "org": org,
            "config": config,
            "template_cfg": template_cfg,
            "all_templates": TEMPLATES_CONFIG
        }
    )
