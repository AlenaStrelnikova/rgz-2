from . import db
from flask_login import UserMixin

# Модель пользователя
class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False)

# Модель товара
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    code = db.Column(db.String(20), unique=True)
    quantity = db.Column(db.Integer)
    paid_quantity = db.Column(db.Integer, default=0)

# Модель заказа
class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    products = db.relationship('OrderProduct', backref='order', lazy=True)
    is_paid = db.Column(db.Boolean, default=False)
    is_draft = db.Column(db.Boolean, default=True)

# Модель товара в заказе
class OrderProduct(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    quantity = db.Column(db.Integer)
    product = db.relationship('Product', backref='order_products')

