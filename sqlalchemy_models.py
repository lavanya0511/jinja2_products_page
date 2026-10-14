from sqlalchemy_database import Base
from sqlalchemy import Column,Integer,String
class Products(Base):
    __tablename__ = "products"
    id = Column(Integer,primary_key=True,autoincrement=True)
    name = Column(String,nullable=False)
    price = Column(Integer,nullable=False)
