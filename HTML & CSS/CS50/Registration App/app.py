from flask import Flask, render_template, request

app = Flask(__name__)

sports = ["basketball", "soccer", "baseball", "hockey", "football"]

Registrants = {}

@app.route("/")
def index():
    return render_template("index.html", sports=sports)

@app.route("/register", methods=["POST"]) 
def register():
    name = request.form.get("name")
    sport = request.form.get("sport").lower()
    
    # Validate Submission
    if not name or sport not in sports:
        return render_template("failure.html", message="You must provide your name and select a sport.")
    
    # Record Submission
    Registrants[name] = sport
    
    # Confirm Registration
    return render_template("success.html", name=name, sport=sport) 