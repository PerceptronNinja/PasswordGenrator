from flask import Flask, render_template, request
from password_generator import generate_password

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    password = None
    if request.method == "POST":
        length = int(request.form.get("length"))
        include_uppercase = "uppercase" in request.form
        include_numbers = "numbers" in request.form
        include_special = "special" in request.form

        password = generate_password(length, include_uppercase, include_numbers, include_special)
    return render_template("index.html", password=password)

if __name__ == "__main__":
    app.run(debug=True)
