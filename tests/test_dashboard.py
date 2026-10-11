import io
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

def test_dashboard_route():
    response = client.get("/")
    assert response.status_code == 200
    assert "2GIS Site Generator" in response.text

def test_upload_csv_file():
    csv_content = "Название;Категория;Город\nООО Вектор;Строительство;Москва"
    file = ("test.csv", io.BytesIO(csv_content.encode("utf-8")), "text/csv")

    response = client.post("/upload", files={"file": file}, follow_redirects=True)
    assert response.status_code == 200
    assert "ООО Вектор" in response.text

def test_delete_all_route():
    db = SessionLocal()
    org = Organization(name="Удаляемая Компания", category="auto")
    db.add(org)
    db.commit()
    db.close()

    response = client.post("/delete-all", follow_redirects=True)
    assert response.status_code == 200
    assert "Удаляемая Компания" not in response.text
