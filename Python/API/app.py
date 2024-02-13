from flask import Flask, jsonify, request
app = Flask(__name__) # Initialize the Flask app
from flask_sqlalchemy import SQLAlchemy

# Set the environment to development - This is not necessary, but it is a good practice
# Could use FLASK_ENV=development and FLASK_APP=app.py in the terminal
app.config['ENV'] = 'development'
app.config['DEBUG'] = True 

# Set the database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app) # Initialize the database

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
    
    def to_dict(self): # Custom method to return a dictionary representation of the object for JSON serialization
        # returns a dictionary representation of the object
        # Example: {'id': 1, 'name': 'John Doe', 'style': 'braids'}
        return {
            'id': self.id,
            'name': self.name,
            'style': self.style
        }   


# I am going to create two different versions of the API, /v1/ - uses the path arguments and /v2/ - uses the query parameters

@app.route('/') # Defined route for the API HTTP request
def index(): # Function to be executed when the route is called
    return 'Hello, World! Welcome to the Booking API!'

# In Flask you can make both 127.0.0.1:5000/bookings and 127.0.0.1:5000/bookings/ return the same result by adding a trailing slash to the route
@app.route('/bookings/') # Defined route for the API HTTP request
def get_all_bookings():
    bookings = Booking.query.all()
    output = [booking.to_dict() for booking in bookings]
    #output = [{'name': booking.name, 'style': booking.style} for booking in bookings] # Explicitly define the dictionary representation of the object
    return jsonify({"bookings": output}) # Flask default status code is 200 if you don't put it in the return statement
    # return {
    #     'bookings': [
    #         {
    #             'id': 1,
    #             'name': 'John Doe',
    #             'style': 'braids'
    #         },
    #         {
    #             'id': 2,
    #             'name': 'Jane Doe',
    #             'style': 'locs'
    #         }
    #     ]
    
    # }
    
@app.route('/bookings/<int:id>/') # Defined route for the API HTTP request
def get_single_booking(id):
    booking = Booking.query.get_or_404(id)
    
    if booking is None:
        return jsonify({'message': 'Booking not found'}), 404

    # If you don't JSONify the object, it will return a string representation of the object (dictionary); not what we want from an API return value
    return jsonify({ # Return the booking as a JSON object to the client 
        'id': booking.id,
        'name': booking.name,
        'style': booking.style
    }), 200 # Return a status code of 200
    
@app.route('/bookings/create/', methods=['GET', 'POST'])
def create_booking():
    try: # Might already exist
        name = request.args.get("name")
        style = request.args.get("style")
        if not name:
            name = "Bob"
            
        if not style:
            style = "Waves"
        try:
            booking = Booking.query.filter_by(name=name).first() # Check if the booking already exists  # style is not checked because it is not unique in the database schema
            if booking:
                return jsonify({'message': 'Booking already exists'}), 400
        except Exception as e:
            raise ValueError(f"Error: {str(e)}")
        
        db.session.add(Booking(name=name, style=style))
        db.session.commit()
        return jsonify({'name': name, 'style': style})   
    except Exception as e:
        raise ValueError(f"Error: {str(e)}")

@app.route('/bookings/del/<int:id>/', methods=['GET', 'DELETE']) # Defined route for the API HTTP request
def delete_booking(id):
    if request.method == 'GET':
        return jsonify({'message': 'Send a DELETE request to delete a booking'}), 200
    try:
        booking = Booking.query.get(id)
        data = booking.to_dict()
        db.session.delete(booking)
        db.session.commit()
        return jsonify({'message': 'Booking deleted successfully', 'deleted': data}), 200
    except Exception as e:
        raise ValueError(f"Error: {str(e)}")

@app.route('/api') # Defined route for the API HTTP request
def api():
    return jsonify({
        'name': 'Python API',
        'version': '1.0.0'
    }), 200 # Return a JSON object to the client with a status code of 200

# Error handling

@app.errorhandler(404) # Not Found - function to handle the error when 404 is returned
def not_found(error):
    # Simple Error for Client is preferred to not expose the server error to the client
    #return jsonify({'error': 'Resource not found'}), 404
    return jsonify({"error": f"Resource not found : \n More Details( {str(error)} )"}), 404



@app.errorhandler(500) # Internal Server Error - function to handle the error when 500 is returned
def server_error(error):
    #return jsonify({'error': 'Server error'}), 500
    return jsonify({"error": f"Server error : \n More Details( {str(error)} )" }), 500


@app.errorhandler(ValueError) # Custom Error - function to handle the error when a ValueError is returned
def handle_value_error(error):
    return jsonify({'error': str(error)}), 400

if __name__ == '__main__': # No need for the whole 'flask run' in terminal if the file is run directly via python3 <filename>
    app.run() # Run the API
    #with app.app_context():
        #db.create_all() # Create the database tables once the app is run
        #app.run(debug=True)