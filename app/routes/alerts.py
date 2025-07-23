from flask import Blueprint, jsonify
from app.models.product import Product

alerts_bp = Blueprint("alerts", __name__)

@alerts_bp.route("/low-stock", methods=["GET"])
def low_stock_alerts():
    threshold = 10  # assumed business rule
    low_stock_products = Product.query.filter(Product.stock < threshold).all()
    alerts = [{
        "product_name": p.name,
        "sku": p.sku,
        "stock": p.stock,
        "warehouse": p.warehouse.location
    } for p in low_stock_products]
    return jsonify({"low_stock_alerts": alerts})
