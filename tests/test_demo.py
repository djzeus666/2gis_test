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
    assert "+7 (999) 111-22-33" in response.text
    assert "CAD-Чертеж" in response.text or "Интерактивный" in response.text

def test_all_10_templates_rendering():
    db = SessionLocal()
    org = Organization(
        id="test-org-templates",
        name="СтройГрупп",
        category="construction",
        city="Санкт-Петербург",
        phone="+7 (812) 555-44-33"
    )
    db.add(org)
    db.commit()
    db.close()

    for t_id in range(1, 11):
        response = client.get(f"/demo/test-org-templates?template={t_id}")
        assert response.status_code == 200
        assert "СтройГрупп" in response.text
        assert f"Шаблон #{t_id}" in response.text or f"#{t_id}" in response.text

def test_all_categories_interactive_rendering():
    db = SessionLocal()
    categories = ["auto", "construction", "beauty", "medical", "store", "general"]
    for cat in categories:
        org = Organization(
            id=f"test-org-{cat}",
            name=f"Компания {cat.upper()}",
            category=cat,
            city="Москва"
        )
        db.add(org)
    db.commit()
    db.close()

    for cat in categories:
        response = client.get(f"/demo/test-org-{cat}")
        assert response.status_code == 200
        assert f"Компания {cat.upper()}" in response.text
        assert "blueprint-section" in response.text

def test_demo_landing_404():
    response = client.get("/demo/non-existent-id")
    assert response.status_code == 404
