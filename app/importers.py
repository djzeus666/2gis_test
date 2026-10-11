import csv
import json
import io
from typing import List, Dict, Any
from sqlalchemy.orm import Session
from app.models import Organization

CATEGORY_MAPPING = {
    "авто": "auto",
    "сто": "auto",
    "строй": "construction",
    "строит": "construction",
    "ремонт": "construction",
    "отделк": "construction",
    "магаз": "store",
    "одежд": "store",
    "продукт": "store",
    "электроник": "store",
    "ритейл": "store",
    "торгов": "store",
    "красот": "beauty",
    "парикмах": "beauty",
    "барбер": "beauty",
    "космет": "beauty",
    "салон": "beauty",
    "медиц": "medical",
    "клиник": "medical",
    "стоматолог": "medical",
    "аптек": "medical",
    "врач": "medical",
    "здоров": "medical"
}

def normalize_category(raw_category: str) -> str:
    if not raw_category:
        return "general"
    cat_lower = str(raw_category).strip().lower()
    for key, mapped in CATEGORY_MAPPING.items():
        if key in cat_lower:
            return mapped
    return "general"

def parse_csv_data(content: str, category_override: str = None) -> List[Dict[str, Any]]:
    # Detect delimiter
    sample = content[:2000]
    delimiter = ';' if ';' in sample and sample.count(';') > sample.count(',') else ','

    reader = csv.DictReader(io.StringIO(content), delimiter=delimiter)
    records = []

    for row in reader:
        # Normalize key names (handling Russian and English variants)
        lowered_row = {str(k).strip().lower(): str(v or "").strip() for k, v in row.items() if k}

        name = lowered_row.get('name') or lowered_row.get('название') or lowered_row.get('организация') or lowered_row.get('title') or 'Компания'
        raw_cat = lowered_row.get('category') or lowered_row.get('категория') or lowered_row.get('рубрика') or 'Общие услуги'
        city = lowered_row.get('city') or lowered_row.get('город') or ''
        address = lowered_row.get('address') or lowered_row.get('адрес') or ''
        phone = lowered_row.get('phone') or lowered_row.get('телефон') or lowered_row.get('контакты') or ''
        email = lowered_row.get('email') or lowered_row.get('почта') or ''
        website = lowered_row.get('website') or lowered_row.get('сайт') or ''
        description = lowered_row.get('description') or lowered_row.get('описание') or ''
        working_hours = lowered_row.get('working_hours') or lowered_row.get('часы работы') or lowered_row.get('режим работы') or ''

        final_category = category_override if (category_override and category_override not in ("auto_detect", "none", "")) else normalize_category(raw_cat)
        records.append({
            "name": name,
            "category": final_category,
            "raw_category": raw_cat,
            "city": city,
            "address": address,
            "phone": phone,
            "email": email,
            "website": website,
            "description": description,
            "working_hours": working_hours
        })
    return records

def parse_json_data(content: str, category_override: str = None) -> List[Dict[str, Any]]:
    data = json.loads(content)
    if isinstance(data, dict):
        if "items" in data:
            data = data["items"]
        elif "organizations" in data:
            data = data["organizations"]
        else:
            data = [data]

    records = []
    for item in data:
        name = item.get('name') or item.get('название') or item.get('title') or 'Компания'
        raw_cat = item.get('category') or item.get('категория') or item.get('rubric') or 'Общие услуги'
        city = item.get('city') or item.get('город') or ''
        address = item.get('address') or item.get('адрес') or ''
        phone = item.get('phone') or item.get('телефон') or ''
        email = item.get('email') or item.get('почта') or ''
        website = item.get('website') or item.get('сайт') or ''
        description = item.get('description') or item.get('описание') or ''
        working_hours = item.get('working_hours') or item.get('часы работы') or ''

        final_category = category_override if (category_override and category_override != "auto") else normalize_category(raw_cat)
        records.append({
            "name": name,
            "category": final_category,
            "raw_category": raw_cat,
            "city": city,
            "address": address,
            "phone": phone,
            "email": email,
            "website": website,
            "description": description,
            "working_hours": working_hours,
            "extra_data": item.get('extra') or item.get('2gis_meta') or {}
        })
    return records

def import_organizations_to_db(db: Session, records: List[Dict[str, Any]]) -> int:
    count = 0
    for rec in records:
        raw_cat = rec.pop("raw_category", None)
        extra = rec.get("extra_data") or {}
        if raw_cat:
            extra["raw_category"] = raw_cat

        org = Organization(
            name=rec.get("name"),
            category=rec.get("category", "general"),
            city=rec.get("city"),
            address=rec.get("address"),
            phone=rec.get("phone"),
            email=rec.get("email"),
            website=rec.get("website"),
            description=rec.get("description"),
            working_hours=rec.get("working_hours"),
            extra_data=extra
        )
        db.add(org)
        count += 1
    db.commit()
    return count
