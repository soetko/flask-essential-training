from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    user = {'username': 'Natasha'}
    items = ['Item 1', 'Item 2', 'Item 3']
    return render_template('index.html', user=user, items=items)

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

if __name__ == '__main__':
    app.run(debug=True)
