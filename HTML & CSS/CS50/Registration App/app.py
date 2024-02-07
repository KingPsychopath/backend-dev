from flask import Flask, render_template, request, redirect
from SQL import Database as sQL

app = Flask(__name__)

sports = ["basketball", "soccer", "baseball", "hockey", "football"]

REGISTRANTS = {}
db = sQL('./model/registrants.db')

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
    
    REGISTRANTS[name] = sport
    db.insert_data('players', {'name': name, 'sport': sport})
    
    # Confirm Registration
    return redirect("/registrants")
    #return render_template("success.html", name=name, sport=sport) 


@app.route("/registrants")
def registrants():
    return render_template("registrants.html", registrants=REGISTRANTS)