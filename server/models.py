import datetime
from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.orm import validates
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy

metadata = MetaData(naming_convention={
    'fk': 'fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s',
})

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

db = SQLAlchemy(metadata=metadata)

CORS(app)
api = Api(app)
db.init_app(app)
migrate = Migrate(app, db)

class Customer(db.Model, SerializerMixin):
    __tablename__ = 'customers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String)
    password = db.Column(db.String)
    phone_number = db.Column(db.Integer)
    updated_at = db.Column(db.DateTime, onupdate=datetime.datetime.utcnow)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    reservations = db.relationship('Reservation', backref='customer')

    serialize_rules = ('-reservations.customer', '-shops.customers')


    @validates('name')
    def validate_name(self, key, value):
        if len(value) < 1 or len(value) > 20:
            raise ValueError('Please enter a Name between 1-20 characters')
        return value

    @validates('email')
    def validate_email(self, key, value):
        if len(value) < 7 and not '@' in value:
            raise ValueError('Please enter a valid Email')
        return value

    @validates('password')
    def validate_password(self, key, value):
        if len(value) < 1:
            raise ValueError('Please enter a Password')
        return value

    def __repr__(self):
        return f'<user name:{self.name}, email:{self.email}>'

class Shop(db.Model, SerializerMixin):
    __tablename__ = 'shops'

    id = db.Column(db.Integer, primary_key=True)
    img = db.Column(db.String)
    neighborhood = db.Column(db.String)
    address = db.Column(db.Varchar)
    updated_at = db.Column(db.DateTime, onupdate=datetime.datetime.utcnow)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    reservations = db.relationship('Reservation', backref='shop')
    workers = db.relationship('Worker', backref='shop')

    serialize_rules = ('-reservations.shop', '-customers.shops')

    @validates('img')
    def validate_img(self, key, value):
        if len(value) < 0:
            raise ValueError('Please enter an Image')
        return value
    
    @validates('neighborhood')
    def validate_img(self, key, value):
        if len(value) < 0:
            raise ValueError('Please enter a valid neighborhood')
        return value
    
    @validates('address')
    def validate_location(self, key, value):
        if value < 0:
            raise ValueError('Please enter a valid address')
        return value
    
    def __repr__(self):
        return f'<shop location:{self.neighborhood}, address:{self.address}>'

class Worker(db.Model, SerializerMixin):
    __tablename__ = 'workers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Integer)
    phone_number = db.Column(db.Integer)
    role = db.Column(db.String)
    day_rate = db.Column(db.Integer)
    updated_at = db.Column(db.DateTime, onupdate=datetime.datetime.utcnow)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    shop_id = db.Column(db.Integer)

    @validates('name')
    def validate_name(self, key, value):
        if len(value) < 1 or len(value) > 20:
            raise ValueError('Please enter a Name between 1-20 characters')
        return value

    @validates('role')
    def validate_description(self, key, value):
        if value != "santa" and value != "elf":
            raise ValueError('role must be either santa or elf')
        return value
    
    @validates('day_rate')
    def validate_day_rate(self, key, value):
        if value < 0:
            raise ValueError('day_rate must be greater than zero')
        return value

    def __repr__(self):
        return f'<worker name:{self.name}, role:{self.role} day rate:{self.day_rate}>'

# this is my join table
class Reservation(db.Model, SerializerMixin):
    __tablename__ = 'reservations'

    id = db.Column(db.Integer, primary_key=True)
    scheduled_time = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=datetime.datetime.utcnow)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    
    shop_id = db.Column(db.Integer, db.ForeignKey('shops.id'))
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'))

    serialize_rules =('-shop.customers', '-customer.shops', '-customer.reservations', '-shop.reservations')

    @validates('scheduled_time')
    def validate_scheduled_time(self, key, scheduled_time):
        if scheduled_time is not None:
            if scheduled_time.time() < datetime.strptime('09:00', '%H:%M').time() or \
                    scheduled_time.time() > datetime.strptime('19:00', '%H:%M').time():
                raise ValueError('Scheduled time should be between 9 AM and 7 PM')
        return scheduled_time

    __table_args__ = (
        db.CheckConstraint("scheduled_time IS NULL OR (scheduled_time::time >= '09:00:00'::time AND scheduled_time::time <= '19:00:00'::time)", name="check_valid_scheduled_time"),
    )


    def __repr__(self):
        return f'<shop location:{self.shop_id}, customer:{self.customer_id}, time:{self.scheduled_time}>'
