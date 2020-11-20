from sba_api_exam.ext.db import Base
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from 

# db의 있는 것이 Article로 정의 = became entity

class Article(Base):
    __tablename__ = "articles"
    __table_args__ = {'mysql_collate' : 'utf8_general_ci'} # 한글 깨짐 방지 encoding

    id = Column(Integer, primary_key=True, index=True)
    user = Column(Integer, ForeignKey("user.id")) # user에 있는 id를 가져와라
    item = Column(Integer, ForeignKey('item.id'))
    title = Column(String)
    content = Column(String)


