from typing import Optional
from fastapi import APIRouter, Depends, HTTPException, Form, status
from pydantic import BaseModel
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Organization, Lead

router = APIRouter()

class LeadCreateSchema(BaseModel):
    organization_id: str
    client_name: str
    phone: str
    comment: Optional[str] = None

@router.post("/api/leads")
def create_lead(
    organization_id: str = Form(...),
    client_name: str = Form(...),
    phone: str = Form(...),
    comment: Optional[str] = Form(None),
    db: Session = Depends(get_db)
):
    org = db.query(Organization).filter(Organization.id == organization_id).first()
    if not org:
        raise HTTPException(status_code=404, detail="Organization not found")

    lead = Lead(
        organization_id=organization_id,
        client_name=client_name,
        phone=phone,
        comment=comment,
        status="new"
    )
    db.add(lead)
    db.commit()
    db.refresh(lead)

    return {
        "status": "ok",
        "lead_id": lead.id,
        "message": "Заявка успешно принята! Менеджер свяжется с вами в течение 5 минут."
    }

@router.post("/admin/leads/{lead_id}/status")
def update_lead_status(
    lead_id: str,
    status: str = Form(...),
    db: Session = Depends(get_db)
):
    lead = db.query(Lead).filter(Lead.id == lead_id).first()
    if not lead:
        raise HTTPException(status_code=404, detail="Lead not found")

    lead.status = status
    db.commit()
    return {"status": "ok", "lead_id": lead.id, "new_status": status}

@router.post("/admin/leads/{lead_id}/delete")
def delete_lead(
    lead_id: str,
    db: Session = Depends(get_db)
):
    lead = db.query(Lead).filter(Lead.id == lead_id).first()
    if not lead:
        raise HTTPException(status_code=404, detail="Lead not found")

    db.delete(lead)
    db.commit()
    return {"status": "ok", "deleted_id": lead_id}
