from flask_restful import Resource,reqparse
from models.user import UserModel

class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username', type=str, required= True, help="This field is required" )
    parser.add_argument('password', type =str, required= True, help="This field is required" )
    def post(self):
        data = UserRegister.parser.parse_args()
        if UserModel.find_by_username(data['username']):
            return {"message" : "A user already exists with the same name"}
        user = UserModel(**data)
        user.save_to_db()
        return {"message":"User registered"},201
    




    