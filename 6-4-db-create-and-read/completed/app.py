from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from forms import MyForm

app = Flask(__name__)
app.secret_key = 'supersecretkey'  

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///health_tracker.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    email = db.Column(db.String(150), nullable=False, unique=True)

    def __repr__(self):
        return f'<User {self.username}>'

@app.route('/form', methods=['GET', 'POST'])
def form():
    form = MyForm()
    if request.method == 'POST' and form.validate_on_submit():
        username = form.username.data
        email = form.email.data

        new_user = User(username=username, email=email)
        db.session.add(new_user) # stage the new user for addition
        db.session.commit() # save the new user to the database

        return redirect(url_for('success', username=username, email=email))
    return render_template('form.html', form=form)

@app.route('/success')
def success():
    #retrieve username and email from the URL query string
    username = request.args.get('username') 
    email = request.args.get('email')
    return render_template('success.html', username=username, email=email)

@app.route('/users')
def users():
    #retrieve all records from the User table in the db
    all_users = User.query.all()
    return render_template('users.html', users=all_users)

if __name__ == '__main__':
    app.run(debug=True)

