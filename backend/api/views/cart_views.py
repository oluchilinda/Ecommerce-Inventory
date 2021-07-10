
import os

from flask import (Blueprint, flash, jsonify, redirect, request, session,
                   url_for)

from ..models import Product
from flask import current_app


cart_main = Blueprint('cart_main', __name__)


@cart_main.route("/cart/<int:product_id>", methods=["POST"])
def add_to_cart(product_id):

    products = Product.query.filter_by(id=product_id).first()
    quantity = int(request.values["quantity"])
    overide = True if request.values["overide"] == 'True' else False
    cart = session.get('cart')
    if not cart:
        cart = session['cart'] = {}
    product_id = str(products.id)
    if product_id not in cart.keys():
        cart[product_id] = {'quantity': 0, 'price': str(products.price)}
    if overide:
        cart[product_id]['quantity'] += quantity
    else:
        cart[product_id]['quantity'] = quantity
    session.modified = True

    return redirect(url_for('cart_main.cart_detail'))


@cart_main.route("/cart/cart_detail", methods=["GET"])
def cart_detail():

    cart = session.get('cart')
    return jsonify({"cart": cart})


@cart_main.route("/cart/cart_remove/<int:product_id>", methods=["GET"])
def cart_remove(product_id):

    product = Product.query.filter_by(id=product_id).first()
    product_id = str(product.id)
    cart = session.get('cart')
    if product_id in cart.keys():
        del cart[product_id]
        session.modified = True
    return redirect(url_for('cart_main.cart_detail'))


@cart_main.route("/cart/decrement/<int:product_id>", methods=["GET"])
def cart_decrement(product_id):
    product_id = str(Product.query.filter_by(id=product_id).first().id)
    cart = session.get('cart')
    if product_id in cart.keys():
        if (cart[product_id]['quantity'] < 1):
            return "no_item"
        else:
            cart[product_id]['quantity'] -= 1
            session.modified = True
            return jsonify({"cart": cart})
    else:
        return jsonify({"cart": cart})


@cart_main.route("/cart/total_amount", methods=["GET"])
def cart_total_amount():
    cart = session.get('cart')
    total_payment = sum(float(item['price']) *
                        item['quantity'] for item in cart.values())
    total_qty = sum(item['quantity'] for item in cart.values())
    return {
        "total_qty": total_qty,
        'total': total_payment
    }


@cart_main.route("/cart/amount", methods=["GET"])
def cart_get_individual_amount():
    cart = session.get('cart')
    for i in cart.keys():
        cart[i]['total_sum'] = float(cart[i]['price']) * cart[i]['quantity']
    return cart
