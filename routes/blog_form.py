from flask import Blueprint,render_template,request,redirect
import database
from datetime import datetime
import re
import hashlib
db = database.db
# Create a blueprint instance
blog_form_bp = Blueprint('blog_form', __name__)

@blog_form_bp.route('/')
def get_blog_form():
    return render_template('blog_form.html')

@blog_form_bp.route('/submit-blog', methods=['POST'])
def submit_blog():

    title = request.form['title']
    headline =  request.form['headline']
    author = request.form['author']
    content = request.form['content']  # This will contain raw HTML
    tags = request.form['tags']
    bgimg = request.form['bgimg']


    slug = slugify(title)
    unique_part = short_hash(title + str(datetime.utcnow()))
    full_url = f"{slug}-{unique_part}"

    data = {"title": title,
            "author": author, 
            "content": content,
            "bgimg":bgimg,
            "tags":tags,
            "headline":headline,
            "url":full_url,
             "timestamp": datetime.utcnow()  # Use UTC for consistency
            }
    upload = db.insert_one(data)

    # Save to database or file (omitted)
    return redirect(f'/blog/{full_url}')



def slugify(text):
    text = re.sub(r'[^\w\s-]', '', text).strip().lower()
    return re.sub(r'[-\s]+', '-', text)

def short_hash(text):
    return hashlib.sha1(text.encode()).hexdigest()[:5]