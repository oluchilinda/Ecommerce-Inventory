

import os

from flask import (Blueprint, flash, jsonify, redirect, request)

from werkzeug.utils import secure_filename
from ..models import Category, Product
from slugify import slugify
from .. import db
from os.path import join, dirname, realpath

product_main = Blueprint('product_main', __name__)


UPLOAD_FOLDER = join(dirname(realpath(__file__)), 'uploads')
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@product_main.route("/category", methods=["POST"])
def add_category():
    name = request.values["name"]
    category_data = Category.query.filter_by(name=name).first()
    if category_data:
        return jsonify({"msg": "category already exist"}), 400
    else:
        category_slug = slugify(name, to_lower=True)
        category = Category(name=name, slug=category_slug)
        db.session.add(category)
        db.session.commit()
        return jsonify({"msg": "category created"}), 201


@product_main.route("/product", methods=["POST","GET"])
def add_product():
    if request.method == 'POST':

        category = request.values["category"]
        description = request.values["description"]
        name = request.values["name"]
        price = float(request.values["price"])
        available = True if request.values["available"]  == 'True' else False
       

        category = Category.query.filter_by(name=category).first().id
        slug = slugify(name, to_lower=True)

        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        uploaded_file = request.files['file']
        filename = secure_filename(uploaded_file.filename)
        if filename != '' and allowed_file(uploaded_file.filename):

            uploaded_file.save(os.path.join(UPLOAD_FOLDER, filename))
            path = os.path.join(UPLOAD_FOLDER, filename)

            product = Product(name=name, slug=slug, category_id=category, image_path=path,
                            description=description, price=price, available=available)
            db.session.add(product)
            db.session.commit()

            return jsonify({"msg": "created_image"}), 201
    if request.method == 'GET':

        products = Product.query.all()
        if products:
            data = [product.serialize for product in products]

            return {"data": data}, 200
        return {"msg": "no products available"}, 400
    
    
@product_main.route("/product/<int:id>/<slug>", methods=["GET"])
def single_product_details(id, slug):
    product = Product.query.filter_by(id=id, slug=slug).first()
    return jsonify(product.serialize)


# @product_main.route('/uploads/<name>')
# def download_file(name):
#     return send_from_directory(UPLOAD_FOLDER, name)
