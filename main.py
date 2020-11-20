from flask import Flask
from flask_restful import Api
from sba_api_exam.ext.db import url, db
from sba_api_exam.ext.routes import initialize_routes
from sba_api_exam.resources.item import Item, Items
from sba_api_exam.resources.article import Article, Articles
from sba_api_exam.resources.user import User, Users
from flask_cors import CORS

print('==============1=============')
app = Flask(__name__)
CORS(app, resources={r'/api/*': {"origins": "*"}})

app.config['SQLALCHEMY_DATABASE_URI'] = url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
api = Api(app)

with app.app_context():
    db.create_all()
with app.app_context():
    count = UserDao.count()
    print(f'>>>>>>>>> Users Total Count is {count}')
    if count == 0:
        UserDao.insert_many()

# @app.before_first_request
# def create_tables():
#     db.create_all()

# reset route
initialize_routes(api)

# with app.app_context():
#     db.create_all()

# @app.route('/api/test')
# def test():
#     return{'test':'SUCCESS'}