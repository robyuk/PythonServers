#! /bin/env /usr/bin/python3
"""An example of a simple blog server in Python using Flask with
endpoints to create, read, update, and delete
blog entries stored in blogs/ba.json.
This version of the blog server uses a Jinja2 template to render the
blog entries in an HTML page.
"""

import os
import json
from datetime import datetime
from flask import Flask, request, jsonify, render_template
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

# Initialize the Flask application
app = Flask(__name__)
auth = HTTPBasicAuth()

# Path to the JSON file where blog entries are stored
BLOG_FILE = 'blogs/ba.json'

# In-memory user storage for demonstration purposes
users = {
    "admin": generate_password_hash("secret")
}

@auth.verify_password
def verify_password(username, password):
    """The verify_password function checks the username and password
    against the in-memory user storage. You can replace this with a
    more secure user management system as needed.
    """
    if username in users and check_password_hash(users.get(username), password):
        return username

def load_blogs():
    """Load blog entries from the JSON file."""
    if not os.path.exists(BLOG_FILE):
        return []
    with open(BLOG_FILE, 'r') as file:
        return json.load(file)

def save_blogs(blogs):
    """Save blog entries to the JSON file."""
    with open(BLOG_FILE, 'w') as file:
        json.dump(blogs, file, indent=4)

@app.route('/blogs', methods=['GET'])
@auth.login_required
def get_blogs():
    """Endpoint to get all blog entries."""
    blogs = load_blogs()
    return render_template('blog.html', posts=blogs)

@app.route('/blogs', methods=['POST'])
@auth.login_required
def create_blog():
    """Endpoint to create a new blog entry."""
    if request.is_json:
        new_blog = request.json
    else:
        new_blog = {
            'title': request.form['title'],
            'content': request.form['content']
        }
    blogs = load_blogs()
    new_blog['id'] = max([blog['id'] for blog in blogs], default=0) + 1
    new_blog['created_at'] = datetime.now().isoformat()
    new_blog['updated_at'] = new_blog['created_at']
    blogs.append(new_blog)
    save_blogs(blogs)
    if request.is_json:
        return jsonify(new_blog), 201
    else:
        return render_template('show1blog.html', post=new_blog)

@app.route('/new_blog', methods=['GET'])
@auth.login_required
def new_blog():
    """Endpoint to render the new blog form."""
    return render_template('new_blog.html')


@app.route('/blogs/<int:id>', methods=['GET'])
@auth.login_required
def get_blog(id):
    """Endpoint to get a specific blog entry by ID."""
    blogs = load_blogs()
    blog = next((blog for blog in blogs if blog['id'] == id), None)
    return render_template('show1blog.html', post=blog) if blog else (f'Blog post with id {id} not found', 404)

@app.route('/blogs/<int:id>', methods=['PUT'])
@auth.login_required
def update_blog(id):
    """Endpoint to update an existing blog entry by ID."""
    updated_blog = request.json
    blogs = load_blogs()
    blog = next((blog for blog in blogs if blog['id'] == id), None)
    if blog:
        blog.update(updated_blog)
        blog['updated_at'] = datetime.now().isoformat()
        save_blogs(blogs)
        return jsonify(blog)
    return ('', 404)

@app.route('/blogs/<int:id>', methods=['DELETE'])
@auth.login_required
def delete_blog(id):
    """Endpoint to delete a blog entry by ID."""
    blogs = load_blogs()
    blogs = [blog for blog in blogs if blog['id'] != id]
    save_blogs(blogs)
    return ('', 204)

if __name__ == '__main__':
    # Run the Flask application in debug mode
    app.run(debug=True)