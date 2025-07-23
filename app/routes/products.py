from flask import Blueprint, request, jsonify
from app.models.product import Product
from app.models.warehouse import Warehouse
from app.utils.db import db

products_bp = Blueprint("products", __name__)

@products_bp.route("/products", methods=["POST"])
def add_product():
    data = request.get_json()
    warehouse = Warehouse.query.filter_by(location=data["warehouse"]).first()
    if not warehouse:
        warehouse = Warehouse(location=data["warehouse"])
        db.session.add(warehouse)
        db.session.commit()
    try:
        product = Product(
            name=data["name"],
            sku=data["sku"],
            price=float(data["price"]),
            stock=int(data["stock"]),
            warehouse=warehouse
        )
        db.session.add(product)
        db.session.commit()
        return jsonify({"message": "Product added successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@products_bp.route("/seed", methods=["GET"])
def seed_products():
    sample_products = [
        {"name": "Mouse", "sku": "M001", "price": 200, "stock": 5, "warehouse": "Mumbai"},
        {"name": "Keyboard", "sku": "K002", "price": 500, "stock": 20, "warehouse": "Delhi"},
        {"name": "Monitor", "sku": "MN003", "price": 7000, "stock": 2, "warehouse": "Bangalore"}
    ]
    for item in sample_products:
        warehouse = Warehouse.query.filter_by(location=item["warehouse"]).first()
        if not warehouse:
            warehouse = Warehouse(location=item["warehouse"])
            db.session.add(warehouse)
            db.session.commit()

        p = Product(
            name=item["name"],
            sku=item["sku"],
            price=item["price"],
            stock=item["stock"],
            warehouse=warehouse
        )
        db.session.add(p)
    db.session.commit()
    return jsonify({"message": "Sample data seeded"})
