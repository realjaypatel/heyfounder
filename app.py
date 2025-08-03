from routes.home import home_bp
from routes.blog import blog_bp
from routes.blog_form import blog_form_bp
from routes.search import search_bp
from flask import Flask
app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024

app.register_blueprint(home_bp)
app.register_blueprint(blog_bp, url_prefix='/blog')
app.register_blueprint(search_bp, url_prefix='/search')
app.register_blueprint(blog_form_bp, url_prefix='/blog_form')



if __name__ == '__main__':
    app.run(debug=True)