##Useful for large apps with multiple features.
from flask import Blueprint

stock_bp = Blueprint("stock", __name__)

@stock_bp.route("/")
def stock_home():
    return "Stock Market Data"
