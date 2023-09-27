from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from model.base import Base
from model.clock_punch import ClockPunch

engine = create_engine(
    "sqlite:///database/db.sqlite3?check_same_thread=False", echo=False
)
Session = sessionmaker(bind=engine)

if not database_exists(engine.url):
    create_database(engine.url)

Base.metadata.create_all(engine)
