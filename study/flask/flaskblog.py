from flask import Flask, render_template, flash, redirect, url_for

from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'f41f71d0e0d6d8b176dd086200a16e43'

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
