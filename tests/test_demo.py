import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.database import Base, engine, SessionLocal
from app.models import Organization

client = TestClient(app)

@pytest.fixture(autouse=True)
def setup_db():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

def test_demo_landing_rendering():
    db = SessionLocal()
    org = Organization(
        id="test-org-123",
        name="Автосервис Плюс",
        category="auto",
        city="Москва",
        phone="+7 (999) 111-22-33"
    )
    db.add(org)
    db.commit()
    db.close()

    response = client.get("/demo/test-org-123")
    assert response.status_code == 200
    assert "Автосервис Плюс" in response.text
    assert "Автосервис &amp; Детейлинг" in response.text or "Автосервис & Детейлинг" in response.text
    assert "+7 (999) 111-22-33" in response.text

def test_demo_landing_404():
    response = client.get("/demo/non-existent-id")
    assert response.status_code == 404
