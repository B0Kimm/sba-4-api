from sba_api_exam.ext.db import db, Base
from sba_api_exam.user.dto import UserDto
from sba_api_exam.item.dto import ItemDto
# db의 있는 것이 Article로 정의 = became entity


class ArticleDto(db.Model):
    __tablename__ = "articles"
    __table_args__={'mysql_collate':'utf8_general_ci'}

    id: int = db.Column(db.Integer, primary_key=True, index=True)
    title: str = db.Column(db.String(100))
    content: str = db.Column(db.String(500))

    userid: str = db.Column(db.String(30), db.ForeignKey(UserDto.userid))
    item_id: int = db.Column(db.Integer, db.ForeignKey(ItemDto.id))

    def __init__(self, title, content, userid, item_id):
        self.title = title
        self.content = content
        self.userid = userid
        self.item_id = item_id

    def __repr__(self):
        return f'id={self.id}, user_id={self.userid}, item_id={self.item_id},\
            title={self.title}, content={self.content}'

    @property
    def json(self):
        return {
            'id': self.id,
            'userid': self.userid,
            'item_id' : self.item_id,
            'title' : self.title,
            'content' : self.content
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()



