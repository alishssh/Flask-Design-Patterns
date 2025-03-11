#Creates Flask app dynamically (useful for large projects).
#Avoids circular imports.
#Keeps configurations separate.
#Use Case: Useful for large projects where you need multiple configurations.

from flask import Flask

def create_app():
    """Factory function to create and configure a Flask app."""
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "supersecret"
    
    @app.route("/")
    def home():
        return "Hello, Flask Factory Pattern!"
    
    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
