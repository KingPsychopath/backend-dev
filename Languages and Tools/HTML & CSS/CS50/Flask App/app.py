from flask import Flask, render_template, request

app = Flask(__name__)  # create a new Flask instance


@app.route("/")
def index():

    # the thing on the right is the actual variable you want to pass to the template file from above
    return render_template("index.html")


@app.route("/greet", methods=["POST"])
def greet():
    # if name is not provided, set it to "World"

    # requests the name from the URL query string (e.g. ?name=Owen)
    # name = request.args.get("name") # for get requests
    name = request.form.get("name")  # for post requests

    # if name is not provided, set it to "World" - not needed as there is a default value in the request.args.get() method
    # preferred because I can handle the type check server side rather than clientside in the HTML
    if not name:
        name = "World"

    # name=name - thing of the left is the variable you plan to use in the template file
    return render_template("greet.html", name=name)


if __name__ == "__main__":
    app.run(debug=True)  # run the Flask app in debug mode
