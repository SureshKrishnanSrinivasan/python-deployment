from flask_restful import Resource,reqparse
from flask_jwt import jwt_required
from models.items import ItemModel

class Items(Resource):

    def get(self):
        return {'items': list(map(lambda x: x.json(), ItemModel.query.all())) }

class Item(Resource): 
    parser = reqparse.RequestParser()
    parser.add_argument('price', type=float,required = True, help="This field cannot be left blank")
    parser.add_argument('store_id', type=int,required = True, help="This field cannot be left blank")

    @jwt_required()
    def get(self,name):
        try:
            item =  ItemModel.find_by_name(name)
            return item.json()  
        except:
            return {"message": "An error occoured"}
    


    def post(self,name): 
        data = Item.parser.parse_args()
        item = ItemModel.find_by_name(name)
        if item:
            return "An item with the name {} already exists".format(name)
        
        new_item = {
            "name": name,
            "price": data['price'],
            "store_id": data['store_id']
        }
        item = ItemModel(name,**data)
        item.save_to_db()
        return new_item
    
    def put(self,name):
        data = Item.parser.parse_args()
        data = Item.parser.parse_args()
        item = ItemModel.find_by_name(name)
        if item is None:
            item = ItemModel(name, **data)
            
        else:   
            item.price = data['price']
        item.save_to_db()

    
    
    def delete(self,name):
        item = ItemModel.find_by_name(name)
        if item:
            item.remove_to_db()
            return {"message":"Item removed from database"}
        else:
            return {"message": "Such an item doesn't exist in database"}

    
    