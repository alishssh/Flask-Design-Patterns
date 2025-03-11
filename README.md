**Documentation**

Flask DesignPatterns
____________________________________________________________________________________________________________________________

**Overview**
____________________________________________________________________________________________________________________________

Factory Pattern           Multi-instanceapps (e.g., Dev/Test/Prod environments)

Blueprints       Largeapplications (e.g., Auth, Products, Orders)

Singleton         Databaseconnections (PostgreSQL, Redis)

Repository      Cleandatabase access (e.g., Blog, CRM)

Service Layer Businesslogic (e.g., Stock predictions, Payments)

Decorator        Security(e.g., Role-based access, Logging)

Observer         Event-drivenfeatures (e.g., Notifications, Logging)

Adapter           ExternalAPI integrations (e.g., Stripe, PayPal)

✅ For small apps → Factory + Blueprints

✅ For large apps → Repository + Service Layer

✅ For authentication → Decorator

✅ For API integrations → Adapter

✅ For single DB connection → Singleton

**TechStack**
____________________________________________________________________________________________________________________________

Backend (Flask)

Database (PostgreSQL)

**ProjectStructure**
____________________________________________________________________________________________________________________________

/SMTMINTERN/Task6/

│

├── 2. blueprint\_example

│           | ├── app.py

│           |├── auth.py        

│           | ├──stock.py         

│├──1. factory\_pattern.py

│├── 3. singleton\_db.py

│├──4.  repository\_pattern.py

│├── 5. service\_layer.py

│   ├──6.  decorator\_auth.py

│   ├──7.  adapter\_pattern.py

**Step-By-StepImplementation**
____________________________________________________________________________________________________________________________

1.    Factory pattern

1.CreatesFlask app dynamically (useful for large projects).

2.Avoidscircular imports.

3\. Keepsconfigurations separate.

**Use Case:Useful for large projects where you need multiple configurations.**

_Codeexample:_

from flask import Flask

def create\_app():

   """Factory function to create and configure a Flaskapp."""

    app= Flask(\_\_name\_\_)

   app.config\["SECRET\_KEY"\] = "supersecret"

   @app.route("/")

    defhome():

       return "Hello, Flask Factory Pattern!"

   return app

app = create\_app()

if \_\_name\_\_ == "\_\_main\_\_":

   app.run(debug=True)

2.     _BlueprintPattern_

1.Useful for large apps with multiplefeatures.

2.**UseCase: When your project has multiple sections (Auth, Stock, Users, etc.).**

3\. Splits Flask routes into multiple files(modules).

Blueprints   Largeapplications (e.g., Auth, Products, Orders)

Makes tasks in pieces and chunks for moreeffective execution.

**Codeexample:**

1\. app.py

from flask import Flask

from auth import auth\_bp

from stock import stock\_bp

app = Flask(\_\_name\_\_)

\# Register blueprints

app.register\_blueprint(auth\_bp,url\_prefix="/auth")

app.register\_blueprint(stock\_bp,url\_prefix="/stock")

if \_\_name\_\_ == "\_\_main\_\_":

    app.run(debug=True)

2.    auth.py

from flask import Blueprint

auth\_bp = Blueprint("auth",\_\_name\_\_)

@auth\_bp.route("/login")

def login():

   return "Login Page"

3.    stock.py

from flask import Blueprint

stock\_bp = Blueprint("stock",\_\_name\_\_)

@stock\_bp.route("/")

def stock\_home():

   return "Stock Market Data"

4.    singleton\_db.py

1.    Ensures only one database connection instanceexists.

2.    **Use Case:Useful for database connections or logging services.**

_Code example:_

fromflask import Flask

fromflask\_sqlalchemy import SQLAlchemy

classDatabase:

    \_instance = None

    def \_\_new\_\_(cls):

        if cls.\_instance is None:

            cls.\_instance = super(Database,cls).\_\_new\_\_(cls)

            cls.\_instance.db = SQLAlchemy()

        return cls.\_instance

db= Database().db

app= Flask(\_\_name\_\_)

app.config\["SQLALCHEMY\_DATABASE\_URI"\]= 'postgresql://postgres:Alish@123@localhost/postgres'

db.init\_app(app)

if\_\_name\_\_ == "\_\_main\_\_":

    app.run(debug=True)

4\. Repository Pattern.

1\. Separates data logic from views, making code cleaner.

2\. Prevents direct database access in routes.

3.    **Use Case:When you need to keep database logic separate from your views.**

_Code example:_

fromflask import Flask, jsonify

fromflask\_sqlalchemy import SQLAlchemy

app= Flask(\_\_name\_\_)

app.config\["SQLALCHEMY\_DATABASE\_URI"\]= 'postgresql://postgres:Alish@123@localhost/postgres'

db= SQLAlchemy(app)

classUser(db.Model):

    id = db.Column(db.Integer,primary\_key=True)

    name = db.Column(db.String(100))

classUserRepository:

    @staticmethod

    def get\_all\_users():

        return User.query.all()

@app.route("/users")

defget\_users():

    users = UserRepository.get\_all\_users()

    return jsonify(\[{"id": u.id,"name": u.name} for u in users\])

if\_\_name\_\_ == "\_\_main\_\_":

    app.run(debug=True)

5.  service\_layer.py

1\. Centralizes business logic inone place.

2\. Keeps route functions clean.

**#UseCase: When your business logic is complex (e.g., stock analysis).**

_Codeexample:_

_fromflask import Flask, jsonify_

_app= Flask(\_\_name\_\_)_

_classStockService:_

    _"""Handles stock businesslogic."""_

    _@staticmethod_

    _def get\_stock\_price(stock\_name):_

        _return {"stock": stock\_name,"price": 100.50}  # Simulatedprice_

_@app.route("/stock/")_

_defstock\_price(name):_

    _return jsonify(StockService.get\_stock\_price(name))_

_if\_\_name\_\_ == "\_\_main\_\_":_

    _app.run(debug=True)_

6\. decorator\_auth.py

1.Modifies function behavior(e.g., authentication).

**#Use Case: For authentication or logging in APIs.**

_Codeexample:_

_fromflask import Flask, request, jsonify_

_app= Flask(\_\_name\_\_)_

_defrequire\_api\_key(f):_

    _def wrapper(\*args, \*\*kwargs):_

        _ifrequest.headers.get("X-API-KEY") != "123456":_

            _return jsonify({"error":"Unauthorized"}), 403_

        _return f(\*args, \*\*kwargs)_

    _return wrapper_

_@app.route("/secure-data")_

_@require\_api\_key_

_defsecure\_data():_

    _return jsonify({"message":"You accessed secure data!"})_

_if\_\_name\_\_ == "\_\_main\_\_":_

    _app.run(debug=True)_

7\. Adapter\_pattern.py

1\. Converts external API datainto your app’s format.

**#UseCase: When integrating third-party APIs (e.g., stock prices, weather data).**

import requests

from flask import Flask, jsonify

app = Flask(\_\_name\_\_)

class StockAPIAdapter:

    """Fetches stock data fromexternal APIs and formats it."""

    @staticmethod

    def get\_stock\_price(symbol):

        response =requests.get(f"https://api.example.com/stocks/{symbol}")

        return {"symbol": symbol,"price": response.json().get("price", 0)}

@app.route("/stock/")

def stock\_price(symbol):

    returnjsonify(StockAPIAdapter.get\_stock\_price(symbol))

if \_\_name\_\_ =="\_\_main\_\_":

    app.run(debug=True)

**Conclusion:**
____________________________________________________________________________________________________________________________

Thisdocumentation helps users to understand flask design patterns with handson codeexample. For more usecases go to other repositories here.
