# import os

# from flask import (Blueprint, flash, jsonify, redirect, request, session)

# from ..models import OrderItem, Order
# from ..utils.cart import Cart
# from .. import db


# order_main = Blueprint('order_main', __name__)


# @order_main.route("/order", methods=["POST",])
# def add_category():
    
#     first_name = request.values["first_name"]
#     last_name = request.values["last_name"]
#     email = request.values["email"]
#     address = request.values["address"]
#     postal_code = request.values["postal_code"]
#     city = request.values["city"]
    
#     order = Order(first_name=first_name,
#                   last_name=last_name,
#                   email=email,
#                   address=address,
#                   postal_code=postal_code,
#                   city=city)
#     order.save()
    
#     cart = session.get('cart')
#     for item in cart:
#         orderItem = OrderItem(
#             order = order,
#             product=item['product'],
#             price=item['price'],
#             quantity=item['quantity']
#         )
        
#         db.session.add(orderItem)
#         db.session.commit()
#     cart.clear()
#     return jsonify({"msg": "order has been fufilled"})
    


