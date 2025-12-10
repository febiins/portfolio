from flask import Flask, render_template, request, redirect, flash, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")

        if not (name and email and message):
            flash("Please fill all fields.", "danger")
            return redirect(url_for("contact"))

        flash("Message sent successfully!", "success")
        print("Message received:", name, email, message)
        return redirect(url_for("contact"))

    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)





