from flask import Blueprint,render_template
from bson import ObjectId
import database
db = database.db
# Create a blueprint instance
blog_bp = Blueprint('blog', __name__)

@blog_bp.route('/')
def get_blog():
    return render_template('blog.html')

@blog_bp.route("/<item_id>")
def get_listing(item_id):
    document = db.find_one({"url": (item_id)})
    return render_template('blog.html',data=document)