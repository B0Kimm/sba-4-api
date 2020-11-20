from flask_restful import Resource
from flask import Response, jsonify
from sba_api_exam.item.dao import Dao

class Item(Resource):
    def __init__(self):
        self.dao = Dao()

    def get(self):
       items = self.dao.select_items()
       return jsonify(items[0])

class Items(Resource):
    ...