from flask import Flask, render_template, request, redirect, url_for
from forms import HealthDataForm

app = Flask(__name__)
app.secret_key = 'you_will_never_guess'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/form', methods=['GET', 'POST'])
def form():
    form = HealthDataForm()
    if request.method == 'POST':
        # Process form data here
        return redirect(url_for('dashboard'))
    return render_template('form.html', form=form)


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


if __name__ == '__main__':
    app.run(debug=True)
