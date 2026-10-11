import pytest
from app.database import Base, engine, SessionLocal
from app.importers import parse_csv_data, parse_json_data, import_organizations_to_db
from app.models import Organization

@pytest.fixture(autouse=True)
def setup_db():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

def test_parse_csv_data():
    csv_content = """Название;Категория;Город;Адрес;Телефон;Email
Автотехцентр 24;Автосервис;Москва;ул. Ленина 10;+79990000000;info@auto24.ru
СтройКомплект;Строительные материалы;СПб;Невский 5;+78120000000;sale@stroy.ru
"""
    records = parse_csv_data(csv_content)
    assert len(records) == 2
    assert records[0]["name"] == "Автотехцентр 24"
    assert records[0]["category"] == "auto"
    assert records[1]["name"] == "СтройКомплект"
    assert records[1]["category"] == "construction"

def test_parse_csv_data_category_override():
    csv_content = """Название;Категория;Город
Компания Разная;Разное;Москва
"""
    records = parse_csv_data(csv_content, category_override="beauty")
    assert len(records) == 1
    assert records[0]["category"] == "beauty"

def test_parse_json_data():
    json_content = """[
        {"название": "Салон Красоты EVA", "категория": "Салон красоты", "город": "Казань"},
        {"название": "Маркет 24", "категория": "Продуктовый магазин", "город": "Москва"}
    ]"""
    records = parse_json_data(json_content)
    assert len(records) == 2
    assert records[0]["category"] == "beauty"
    assert records[1]["category"] == "store"

def test_import_to_db():
    db = SessionLocal()
    csv_content = "Название,Категория,Телефон\nСтоматология Улыбка,Медицина,+79001234567"
    records = parse_csv_data(csv_content)
    count = import_organizations_to_db(db, records)
    assert count == 1

    org = db.query(Organization).filter_by(name="Стоматология Улыбка").first()
    assert org is not None
    assert org.category == "medical"
    db.close()
