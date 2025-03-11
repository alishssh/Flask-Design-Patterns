#Ensures only one database connection instance exists.

#Use Case: Useful for database connections or logging services.

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

class Database:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls)
            cls._instance.db = SQLAlchemy()
        return cls._instance

db = Database().db

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://postgres:Alish@123@localhost/postgres'
db.init_app(app)

if __name__ == "__main__":
    app.run(debug=True)
