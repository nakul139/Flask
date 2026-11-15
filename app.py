from flask import Flask 
from uuid import UUID

app = Flask(__name__)

# Static Routing
@app.route("/")
def home():
    return "Home Page"

@app.route("/about")
def about():
    return "Welcome to About Page"

# Dynamic Routing
@app.route("/user/<name>") 
def user(name):
    return f"Welcome {name}"

# Multiple Dynamic Routing
@app.route("/student/<name>/<course>")
def student(name, course):
    return f"{name} is learning {course}"

# URL Converter like int, float, string, path, uuid
@app.route("/users/<int:id>")
def users(id):
    return f"User id: {id}"

@app.route("/price/<float:amount>")
def price(amount):
    return f"Price : {amount}"

@app.route("/name/<string:fullName>")
def name(fullName):
    return f"Name: {fullName}"

@app.route("/files/<path:file_path>")
def file(file_path):
    return file_path 

@app.route("/patient/<uuid:user_id>")
def patient(user_id):
    return str(user_id)



if __name__ == "__main__":
    app.run(debug=True)

