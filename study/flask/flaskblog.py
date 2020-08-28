from flask import Flask, render_template, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'f41f71d0e0d6d8b176dd086200a16e43'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User({self.username}, {self.email}, {self.image_file})"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post({self.title}, {self.date_posted})"

# user_1 = User(username='CreedB', email='creedbratton@dunder.com', password='password')
# user_2 = User(username='RyanWoof', email='ryanhoward@dunder.com', password='ihatekelly')
# post_1 = Post(title='First post', content='Post content', user_id=user.id)
# post_2 = Post(title='Second post', content='Post content', user_id=user.id)


posts = [
    {
        'author': 'Creed Bratton',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Ryan Howard',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 22, 2018'
    },
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))

    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'Welcome back!', 'success')
        return redirect(url_for('home'))
    return render_template('login.html', title='Login', form=form)


if __name__ == "__main__":
    app.run(debug=True)
