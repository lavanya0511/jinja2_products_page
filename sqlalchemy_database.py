from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

url = "mysql+mysqlconnector://root:Lavanya%400511@localhost:3306/fast_api"

engine = create_engine(url)
LocalSession = sessionmaker(bind=engine,autoflush=True)
Base = declarative_base()
