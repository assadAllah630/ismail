from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# SQLAlchemy instance (to be initialized in app.py)
db = SQLAlchemy()

class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    products = db.relationship('Product', backref='category', lazy=True)

class Tag(db.Model):
    __tablename__ = 'tags'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    products = db.relationship('ProductTag', back_populates='tag')

class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    name_ar = db.Column(db.String(255), nullable=False)
    name_en = db.Column(db.String(255), nullable=False)
    item_uid = db.Column(db.String(255), nullable=False)
    item_code = db.Column(db.String(255), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)
    short_description = db.Column(db.Text, nullable=True)
    total_cost = db.Column(db.Numeric(10,2), nullable=False)
    barcode = db.Column(db.String(255), nullable=True)
    quantity = db.Column(db.Integer, nullable=False)
    inventory_location = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Numeric(10,2), nullable=False)
    cost = db.Column(db.Numeric(10,2), nullable=False)
    photos = db.relationship('ProductPhoto', backref='product', lazy=True)
    tags = db.relationship('ProductTag', back_populates='product')
    media_links = db.relationship('ProductMedia', back_populates='product')

class ProductTag(db.Model):
    __tablename__ = 'product_tags'
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), primary_key=True)
    tag_id = db.Column(db.Integer, db.ForeignKey('tags.id'), primary_key=True)
    product = db.relationship('Product', back_populates='tags')
    tag = db.relationship('Tag', back_populates='products')

class ProductPhoto(db.Model):
    __tablename__ = 'product_photos'
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    photo_url = db.Column(db.String(512), nullable=False)
    uploaded_at = db.Column(db.DateTime, default=datetime.utcnow)

class Media(db.Model):
    __tablename__ = 'media'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    media_type = db.Column(db.Enum('post', 'reel', 'story'), nullable=False)
    description = db.Column(db.Text, nullable=True)
    file_url = db.Column(db.String(512), nullable=False)
    upload_date = db.Column(db.DateTime, default=datetime.utcnow)
    published = db.Column(db.Boolean, default=False)
    products = db.relationship('ProductMedia', back_populates='media')

class ProductMedia(db.Model):
    __tablename__ = 'product_media'
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), primary_key=True)
    media_id = db.Column(db.Integer, db.ForeignKey('media.id'), primary_key=True)
    product = db.relationship('Product', back_populates='media_links')
    media = db.relationship('Media', back_populates='products') 