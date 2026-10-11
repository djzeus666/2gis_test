import uuid
from datetime import datetime
from sqlalchemy import Column, String, Text, DateTime, JSON
from app.database import Base

class Organization(Base):
    __tablename__ = "organizations"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String(255), nullable=False, index=True)
    category = Column(String(100), nullable=False, index=True)  # auto, construction, store, beauty, medical, general
    city = Column(String(100), nullable=True)
    address = Column(String(255), nullable=True)
    phone = Column(String(100), nullable=True)
    email = Column(String(100), nullable=True)
    website = Column(String(255), nullable=True)
    description = Column(Text, nullable=True)
    working_hours = Column(String(255), nullable=True)

    # Custom fields from 2GIS parse (e.g. rating, reviews_count, services list)
    extra_data = Column(JSON, nullable=True, default=dict)

    created_at = Column(DateTime, default=datetime.utcnow)
