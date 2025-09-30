from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Query(Base):
    __tablename__ = 'queries'

    id = Column(Integer, primary_key=True, index=True)
    user_query = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

class Result(Base):
    __tablename__ = 'results'

    id = Column(Integer, primary_key=True, index=True)
    query_id = Column(Integer, nullable=False)
    result_text = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)