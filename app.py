from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    name = request.form.get("name")
    mail = request.form.get("email")
    password = request.form.get("password")
    phone = request.form.get("phone")
    gender = request.form.get("gender")
    course = request.form.get("course")
    address = request.form.get("address")

    return f"Welcome {name}! Your registration is successful."


if __name__ == "__main__":
    app.run(debug=True)