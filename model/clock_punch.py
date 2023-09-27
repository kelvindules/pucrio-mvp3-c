from dataclasses import dataclass
from sqlalchemy import Column, String, Integer, DateTime, TEXT
from datetime import datetime
from model import Base


@dataclass
class ClockPunch(Base):
    id: int
    username: str
    token: str
    created_at: DateTime

    __tablename__ = "clock_punch"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    username = Column("username", String(50))
    token = Column("token", TEXT)
    created_at = Column("created_at", DateTime(timezone=True), default=datetime.now)

    def __init__(self, username, token):
        self.username = username
        self.token = token
