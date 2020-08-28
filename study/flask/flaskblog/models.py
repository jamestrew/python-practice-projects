from datetime import datetime

from flask_login import UserMixin

from flaskblog import db, login_manager


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
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
