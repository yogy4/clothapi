# from conf.base import db
from app import db 
from passlib.hash import pbkdf2_sha256  as sha256
import enum

class SizeCloth(enum.Enum):
    S = "Small"
    M = "Medium"
    L = "Large"
    XL = "Extra Large"

class Baju(db.Model):
    __tablename__ = 'clothes'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    size = db.Column(db.Enum(SizeCloth))
    price = db.Column(db.Integer())
    quantity = db.Column(db.Integer())

    def __init__(self,name,size,price,quantity):
        self.name = name
        self.size = size
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id,
            'name':self.name,
            'size':self.size,
            'price':self.price,
            'quantity':self.quantity
        }

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String())
    email = db.Column(db.String())
    avatar = db.Column(db.String())
    password = db.Column(db.String())

    def __init__(self, name, email, avatar, password):
        self.name = name
        self.email = email
        self.avatar = avatar 
        self.password = password

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'email':self.email,
            'avatar':self.avatar,
            'password':self.password
        }

    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def generate_hash(password):
        return sha256.hash(password)

    @staticmethod
    def verify_hash(password, hash):
        return sha256.verify(password, hash)

class Transaction(db.Model):
    __tablename__ = 'transactions'

    id = db.Column(db.Integer, primary_key = True)
    member_id = db.Column(db.Integer)
    cloth = db.Column(db.String())
    quantity = db.Column(db.Integer)
    total_prices = db.Column(db.Integer)

    def __init__(self, member_id, cloth, quantity, total_prices):
        self.member_id = member_id
        self.cloth = cloth
        self.quantity = quantity 
        self.total_prices = total_prices

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id,
            'member_id': self.member_id,
            'cloth':self.cloth,
            'quantity':self.quantity,
            'total_prices':self.total_prices
        }

    def history(self):
        return {
            'id': self.id,
            'member_id': self.member_id,
            'cloth': self.cloth
        }

    
    