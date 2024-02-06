from flask import Flask, render_template, request

app = Flask(__name__) # create a new Flask instance

@app.route("/")
def index():
    # requests the name from the URL query string (e.g. ?name=Owen)
    name = request.args.get("name")
    
    # if name is not provided, set it to "World"
    if not name:
        name = "World"

    # name=name - thing of the left is the variable you plan to use in the template file
    # the thing on the right is the actual variable you want to pass to the template file from above
    return render_template("index.html", name=name)

if __name__ == "__main__":
    app.run(debug=True) # run the Flask app in debug mode
