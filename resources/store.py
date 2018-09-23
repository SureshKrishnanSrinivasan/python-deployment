from flask_restful import Resource
from models.store import StoreModel

class Store(Resource):
    def get(self,name):
        store =  StoreModel.find_by_name(name)
        if store:
            return {'store': store.json()}
        else:
            return {'message' : 'Store not found'},404
    def post(self,name):
        store =  StoreModel.find_by_name(name)
        if store:
            return {'message' : "Store with name '{}' already exists".format(name)},400
        else:
            try:
                store = StoreModel(name)
                store.save_to_db()
            except:
                return {'message': 'An error occoured'},500

        return {'message' : 'Data sucessfully added to database'}

    def delete(self,name):
        store = StoreModel.find_by_name(name)
        if store:
            store.remove_to_db()
        return {'message' : 'Store removed from database'}


class StoreList(Resource):
    def get(self):
        return {'stores': [item.json() for item in StoreModel.query.all()]}