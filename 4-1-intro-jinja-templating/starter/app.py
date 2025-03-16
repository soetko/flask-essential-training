from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    user = {'username': 'Bruce'}
    return render_template('index.html', title='Home', user=user)


if __name__ == '__main__':
    app.run(debug=True)
