from flask import Blueprint, render_template
import database
db = database.db
# Create a blueprint instance
home_bp = Blueprint('home', __name__)

@home_bp.route('/')
def get_home():
    results = db.aggregate([{"$sample": {"size": 10}}])
    results = [dict(item, _id=str(item["_id"])) for item in results]
    return render_template('home.html',data=results)
