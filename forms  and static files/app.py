from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/login", methods = ["GET", "POST"])
def login():
    if request.method == "POST":
        user = request.form["username"]
        color = request.form["color"]
        return redirect(url_for("greet.html", username =user, color = color))
    return render_template("login.html")

@app.route("/greet", methods=["GET", "POST"])
def greet():
    if request.method == "POST":
        user = request.form["username"]
        color = request.form["color"]
        return render_template("greet.html", username = user, favorite_color = color)
    

if __name__ == "__main__":
    app.run(debug=True)