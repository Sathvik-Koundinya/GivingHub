from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

# Models
class Opportunity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(300), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    location = db.Column(db.String(100), nullable=False)

# Routes
@app.route("/opportunities", methods=["GET"])
def get_opportunities():
    opportunities = Opportunity.query.all()
    return jsonify([{
        "id": opp.id,
        "title": opp.title,
        "description": opp.description,
        "category": opp.category,
        "location": opp.location
    } for opp in opportunities])

@app.route("/opportunities", methods=["POST"])
def add_opportunity():
    data = request.get_json()
    new_opportunity = Opportunity(
        title=data["title"],
        description=data["description"],
        category=data["category"],
        location=data["location"]
    )
    db.session.add(new_opportunity)
    db.session.commit()
    return jsonify({"message": "Opportunity added!"}), 201

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)