from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base
DATABASE_URI = 'sqlite:///students.db'
engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)

Base.metadata.create_all(engine)
