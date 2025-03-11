#Use Case: When your project has multiple sections (Auth, Stock, Users, etc.).

from flask import Flask
from blueprint_example.auth import auth_bp
from blueprint_example.stock import stock_bp

app = Flask(__name__)

# Register blueprints
app.register_blueprint(auth_bp, url_prefix="/auth")
app.register_blueprint(stock_bp, url_prefix="/stock")

if __name__ == "__main__":
    app.run(debug=True)
