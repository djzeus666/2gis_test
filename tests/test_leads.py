import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.database import Base, engine, SessionLocal
from app.models import Organization, Lead

client = TestClient(app)

@pytest.fixture(autouse=True)
def setup_db():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

def test_create_and_manage_leads():
    db = SessionLocal()
    org = Organization(
        id="test-lead-org-1",
        name="Клиника Здоровье",
        category="medical",
        city="Москва"
    )
    db.add(org)
    db.commit()
    db.close()

    # 1. Create lead
    response = client.post("/api/leads", data={
        "organization_id": "test-lead-org-1",
        "client_name": "Мария С.",
        "phone": "+7 (900) 111-22-33",
        "comment": "Запись на Чекап Здоровья"
    })
    assert response.status_code == 200
    res_data = response.json()
    assert res_data["status"] == "ok"
    lead_id = res_data["lead_id"]

    # 2. Check lead appears on admin dashboard
    dash = client.get("/")
    assert dash.status_code == 200
    assert "Мария С." in dash.text
    assert "+7 (900) 111-22-33" in dash.text

    # 3. Update lead status
    status_res = client.post(f"/admin/leads/{lead_id}/status", data={"status": "contacted"})
    assert status_res.status_code == 200

    # 4. Delete lead
    del_res = client.post(f"/admin/leads/{lead_id}/delete")
    assert del_res.status_code == 200
