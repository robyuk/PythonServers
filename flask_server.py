#! /bin/python3
#
from flask import Flask, render_template, send_from_directory, url_for
from datetime import datetime
import os

app = Flask(__name__)

class UserProfile:
    def __init__(self, name, age, bio, interests, favorite_song):
        self.name = name
        self.age = age
        self.bio = bio
        self.interests = interests
        self.favorite_song = favorite_song

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.name

    def __str__(self):
        return f'User {self.name}'

# Create a fake user object
fake_user = UserProfile(
    'Robert',
    30,
    'Software developer with a passion for open-source projects.',
    ['Coding', 'Music', 'Gaming'],
    'Bohemian Rhapsody'
)

@app.route('/')
def index():
    #name = username.name
    return render_template('index.html', name=fake_user)

@app.route('/profile/<username>')
def profile(username):
    user = fake_user
    return render_template('profile.html', name=user.name, age=user.age, bio=user.bio, interests=user.interests, favorite_song=user.favorite_song)

@app.route('/datetime')
def get_datetime():
    return 'The current date and time is: {}'.format(datetime.now())

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')



if __name__ == '__main__':
    app.run(port=5000)
