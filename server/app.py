from flask import Flask, make_response, request, jsonify, abort, session
from flask_migrate import Migrate
from flask_restful import Api, Resource

from werkzeug.exceptions import NotFound, Unauthorized
from flask_cors import CORS


from models import db, User, Worker, Shop, Reservation

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False
app.config['SECRET_KEY'] = "abcd"


api = Api(app)
db.init_app(app)
migrate = Migrate(app, db)

#/users
class Users(Resource):
    #GET
    def get(self):
        return make_response([user.to_dict(rules=('-reservations',)) for user in User.query.all()], 200)
    
    #POST
    def post(self):
        try:
            r_json = request.get_json()
            new_user = User(
                name = r_json['name'],
                email = r_json['email'],
                password = r_json['password']
            )

            db.session.add(new_user)
            db.session.commit()
            session['user_id'] = new_user.id

            return make_response(jsonify(new_user.to_dict()), 201)
        
        except ValueError as e:
            return make_response({'error': e.__str__()}, 400)

api.add_resource(Users, '/users')

#/users/:id
class UserById(Resource):
    #GET
    def get(self, id):
        user = User.query.filter_by(id = id).first()

        if not user:
            return make_response({'error': 'User Not Found!'}, 404)

        return make_response(user.to_dict(), 200)

    #PATCH
    def patch(self, id):
        user = User.query.filter_by(id= id).first()

        if not user:
            return make_response({'error': 'User Not Found!' }, 404)

        try: 
            r_json = request.get_json()
            for key in r_json:
                setattr(user, key, r_json[key])
        
            db.session.add(user)
            db.session.commit()

            return make_response(user.to_dict(), 200)
        
        except ValueError as e:
            return make_response({'error': e.__str__()}, 400)

    #DELETE
    def delete(self, id):
        user = User.query.filter_by(id = id).first()

        if not user:
            return make_response({'error': 'User Not Found!'}, 404)

        [db.session.delete(reservation) for reservation in Reservation.query.filter(Reservation.user_id == user.id).all()]

        db.session.delete(user)
        db.session.commit()

        return make_response('', 204)

api.add_resource(UserById, '/users/<int:id>')

#/games
class Shops(Resource):
    #GET
    def get(self):
        return make_response(jsonify([shop.to_dict() for shop in Shop.query.all()]), 200)

    #POST
    def post(self):
        try:
            r_json = request.get_json()
            new_shop = Shop(
                img = r_json['image'],
                price = r_json['price'],
                genre = r_json['genre'],
                title = r_json['title'],
                studio = r_json['studio'],
                description = r_json['description']
            )

            db.session.add(new_shop)
            db.session.commit()

            return make_response(jsonify(new_shop.to_dict()), 201)
        except ValueError as e:
            return make_response({'error': e.__str__()}, 400)

api.add_resource(Shops, '/shops')

#/games/:id
class ShopById(Resource):
    #GET
    def get(self, id):
        return make_response(Shop.query.filter_by(id = id).first().to_dict(), 200)

    #PATCH
    def patch(self, id):
        shop = Shop.query.filter_by(id = id).first()

        if not shop:
            return make_response({ 'error': 'Shop Not Found!'}, 404)

        try:
            r_json = request.get_json()
            for key in r_json:
                setattr(shop, key, r_json[key])
        
            db.session.add(shop)
            db.session.commit()

            return make_response(shop.to_dict(), 200)
        except ValueError as e:
            return make_response({'error': e.__str__()}, 400)

    #DELETE
    def delete(self, id):
        shop = Shop.query.filter_by(id = id).first()

        if not shop:
            return make_response({'error': 'Game Not Found!'}, 404)

        [db.session.delete(reservation) for reservation in Reservation.query.filter(Reservation.game_id == shop.id).all()]
        
        db.session.delete(shop)
        db.session.commit()

        return make_response('', 204)

api.add_resource(ShopById, '/shops/<int:id>')

#/reviews
class Reservations(Resource):

    #GET
    def get(self):
        return make_response(jsonify([reservation.to_dict() for reservation in Reservation.query.all()]), 200)

    #POST
    def post(self):
        try:
            r_json = request.get_json()
            new_reservation = Reservation(
                rating = r_json['rating'],
                scheduled_time = r_json['scheduled_time'],
                shop_id = r_json['shop_id'],
                user_id = r_json['user_id']
            )

            user = User.query.filter(User.id == new_reservation.user_id).first()
            shop = Shop.query.filter(Shop.id == new_reservation.shop_id).first()

            if not user or not shop:
                return make_response({'error': 'Invalid Shop or User ID!'}, 400)

            db.session.add(new_reservation)
            db.session.commit()

            return make_response(jsonify(new_reservation.to_dict()), 201)
        except ValueError as e:
            return make_response({'error': e.__str__()}, 400)

api.add_resource(Reservations, '/reservations')

#/reviews/:id
class ReservationById(Resource):
    #DELETE
    def delete(self, id):
        reservation = Reservation.query.filter_by(id = id).first()

        if not reservation:
            return make_response({'error': 'Reservation Not Found!'}, 404)
        
        db.session.delete(reservation)
        db.session.commit()

        return make_response('', 204)

api.add_resource(ReservationById, '/reservations/<int:id>')

#/usergames
class Workers(Resource):

    #GET
    def get(self):
        return make_response(jsonify([worker.to_dict() for worker in Worker.query.all()]), 200)

    #POST
    def post(self):
        try:
            r_json = request.get_json()
            new_worker = Worker(
                name = r_json['name'],
                role = r_json['role'],
                day_rate = r_json['day_rate'],
                shop_id = r_json['shop_id']
            )

            db.session.add(new_worker)
            db.session.commit()
            session['worker_id'] = new_worker.id

            return make_response(jsonify(new_worker.to_dict()), 201)
        
        except ValueError as e:
            return make_response({'error': e.__str__()}, 400)

api.add_resource(Workers, '/workers')

#/worker/:id
class WorkerById(Resource):

    #GET
    def get(self, id):
        worker = Worker.query.filter_by(id = id).first()

        if not worker:
            return make_response({'error': 'Worker Not Found!'}, 404)

        return make_response(worker.to_dict(), 200)

    #PATCH
    def patch(self, id):
        worker = Worker.query.filter_by(id = id).first()

        if not worker:
            return make_response({ 'error': 'Worker Not Found!'}, 404)

        try:
            r_json = request.get_json()
            for key in r_json:
                setattr(worker, key, r_json[key])
        
            db.session.add(worker)
            db.session.commit()

            return make_response(worker.to_dict(), 200)
        except ValueError as e:
            return make_response({'error': e.__str__()}, 400)

    #DELETE
    def delete(self, id):
        worker = Worker.query.filter_by(id = id).first()

        if not worker:
            return make_response({'error': 'Worker Not Found!'}, 404)
        
        db.session.delete(worker)
        db.session.commit()

        return make_response('', 204)
    
api.add_resource(WorkerById, '/workers/<int:id>')



class Login(Resource):
    #not sure about this!!################################################################
    def post(self):
        user = User.query.filter_by(name=request.get_json()['name']).first()
        
        if not user:
            return make_response({'error': 'Invalid Username/Password'}, 403)

        session['user_id'] = user.id
        response = make_response(
            user.to_dict(),
            200
        )
        return response
api.add_resource(Login, '/login')

class Logout(Resource):
    def delete(self):
        session['user_id'] = None
        response = make_response('',204)
        return response

api.add_resource(Logout, '/logout')

class AuthorizedSession(Resource):
    def get(self):
        user= User.query.filter_by(id=session.get('user_id')).first()
        if user:
            response = make_response(
                user.to_dict(),
                200
            )
            return response
        else:
            abort(401, "Unauthorized")

api.add_resource(AuthorizedSession, '/authorized')



if __name__ == '__main__':
    app.run(port=5555, debug=True)