from app.models.product import Product
from app.utils.db import db

def get_low_stock_alerts(threshold=10):
    low_stock = Product.query.filter(Product.stock < threshold).all()
    return [{
        "name": p.name,
        "sku": p.sku,
        "stock": p.stock,
        "warehouse": p.warehouse
    } for p in low_stock]
