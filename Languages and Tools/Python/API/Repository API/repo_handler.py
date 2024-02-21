from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

class Repository(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    # Add other fields as per the specification

db.create_all()

@app.route('/repositories', methods=['POST'])
def create_repository():
    data = request.get_json()
    repo = Repository(name=data['name'])  # Add other fields as per the specification
    db.session.add(repo)
    db.session.commit()
    return jsonify({'id': repo.id}), 201

@app.route('/repositories/<int:repo_id>', methods=['GET'])
def get_repository(repo_id):
    repo = Repository.query.get_or_404(repo_id)
    return jsonify({'name': repo.name})  # Add other fields as per the specification

if __name__ == '__main__':
    app.run(debug=True)
