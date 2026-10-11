from fastapi import APIRouter, Depends, File, Form, UploadFile, Request, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Organization
from app.importers import parse_csv_data, parse_json_data, import_organizations_to_db

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

@router.get("/", response_class=HTMLResponse)
def dashboard(request: Request, db: Session = Depends(get_db)):
    organizations = db.query(Organization).order_by(Organization.created_at.desc()).all()
    host_url = str(request.base_url).rstrip('/')
    return templates.TemplateResponse(
        request=request,
        name="dashboard.html",
        context={
            "organizations": organizations,
            "host_url": host_url
        }
    )

@router.post("/upload")
async def upload_file(
    file: UploadFile = File(...),
    category_override: str = Form("auto"),
    db: Session = Depends(get_db)
):
    content_bytes = await file.read()
    content_str = content_bytes.decode("utf-8-sig", errors="ignore")

    filename = file.filename.lower() if file.filename else ""
    if filename.endswith(".json"):
        records = parse_json_data(content_str, category_override=category_override)
    else:
        records = parse_csv_data(content_str, category_override=category_override)

    import_organizations_to_db(db, records)
    return RedirectResponse(url="/", status_code=303)

@router.post("/delete-all")
def delete_all_organizations(db: Session = Depends(get_db)):
    db.query(Organization).delete()
    db.commit()
    return RedirectResponse(url="/", status_code=303)
