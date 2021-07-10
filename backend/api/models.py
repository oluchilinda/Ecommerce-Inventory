

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError, SQLAlchemyError

from . import db


class BaseModel(db.Model):
    """Define the base model for all other models."""

    __abstract__ = True
    id = db.Column(db.Integer(), primary_key=True)
    created_on = db.Column(
        db.DateTime(), server_default=db.func.now(), nullable=False)
    updated_on = db.Column(db.DateTime(), nullable=False,
                           server_default=db.func.now(),
                           onupdate=db.func.now())

    def save(self):
        """Save an instance of the model from the database."""
        try:
            db.session.add(self)
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
        except SQLAlchemyError:
            db.session.rollback()


class Category(BaseModel):
    __tablename__= 'category'

    name = db.Column(db.String())
    slug = db.Column(db.String())
    products = db.relationship('Product', backref='category')

    def __str__(self):
        return self.name


class Product(BaseModel):
    __tablename__='product'

    name = db.Column(db.String())
    slug = db.Column(db.String())
    image_path = db.Column(db.String())
    description = db.Column(db.Text())
    price = db.Column(db.Float())
    available = db.Column(db.Boolean())
    category_id = db.Column(db.Integer(), db.ForeignKey('category.id'))
    order = db.relationship('OrderItem', backref='product')
   
    def __str__(self):
        return self.name

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'slug': self.slug,
            'image_path': self.image_path,
            'description': self.description,
            'price': self.price,
            'available': self.available,

        }


class Order(BaseModel):
    __tablename__= 'order'
    first_name = db.Column(db.String())
    last_name = db.Column(db.String())
    email = db.Column(db.String())
    address = db.Column(db.String())
    postal_code = db.Column(db.String())
    city = db.Column(db.String())
    paid = db.Column(db.Boolean(), default=False)
    order = db.relationship("OrderItem", backref='order')
    
    def __str__(self):
        return f'Order {self.id}'



class OrderItem(BaseModel):
    __tablename__= 'order_item'
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey(
        'product.id'), nullable=False)
    price = db.Column(db.Float())
    quantity = db.Column(db.Integer())

    def __str__(self):
        return str(self.id)
