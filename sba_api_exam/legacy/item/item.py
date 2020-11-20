from sqlalchemy import Column, Integer, String, ForeignKey
from sba_api_exam.ext.db import Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.dialects.mysql import VARCHAR

class Item(Base):
    def __init__(self) :
        __tablename__ = 'item'

        id = Column(Integer, primary_key=True, index=True)
        name = Column(String)
        price = Column(String)



engine = create_engine('mysql+mysqlconnector://root:1793456@127.0.0.1/mariadb?charset=utf8', encoding='utf8', echo=True)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

session.commit()