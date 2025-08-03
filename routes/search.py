from flask import Blueprint, render_template
import re
import database
db = database.db
# Create a blueprint instance
search_bp = Blueprint('search', __name__)


@search_bp.route('/')
def get_search_home():
    return render_template('search.html',data=[])


@search_bp.route('/<search_text>')
def get_search(search_text):
    if not search_text:
        return render_template('search.html',data=[])
    search_filter = {
        "$or": [
            {"title": {"$regex": re.escape(search_text), "$options": "i"}},
            {"content": {"$regex": re.escape(search_text), "$options": "i"}},
            {"tags": {"$regex": re.escape(search_text), "$options": "i"}},
        ]   
    }
    results = db.find(search_filter)
    results = [dict(item, _id=str(item["_id"])) for item in results]
    return render_template('search.html',data=results)