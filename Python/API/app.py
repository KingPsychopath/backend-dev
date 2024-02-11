from flask import Flask
from SQLAlchemy import SQLAlchemy as db
app = Flask(__name__)

# ORM - Object Relational Mapping
# to map the database to the object for easy manipulation
# from flask_sqlalchemy import SQLAlchemy
class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    style = db.Column(db.String(120), unique=False, nullable=False)

    def __repr__(self):
        # returns a string representation of the object
        # Example: <Booking John Doe> 
        return f'<Booking #{self.id} {self.name}: {self.style}>'
    

# Set the environment to development - This is not necessary, but it is a good practice
# Could use FLASK_ENV=development and FLASK_APP=app.py in the terminal
app.config['ENV'] = 'development'
app.config['DEBUG'] = True 

@app.route('/') # Defined route for the API HTTP request
def index(): # Function to be executed when the route is called
    return 'Hello, World!'

@app.route('/bookings') # Defined route for the API HTTP request
def bookings():
    return {
        'bookings': [
            {
                'id': 1,
                'name': 'John Doe',
                'style': 'braids'
            },
            {
                'id': 2,
                'name': 'Jane Doe',
                'style': 'locs'
            }
        ]
    
    }

@app.route('/api') # Defined route for the API HTTP request
def api():
    return {
        'name': 'Python API',
        'version': '1.0.0'
    }

if __name__ == '__main__': # Skip the whole 'flask run' in terminal if the file is run directly
    app.run() # Run the API