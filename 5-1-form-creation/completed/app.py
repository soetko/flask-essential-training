from flask import Flask, render_template, request
from forms import MyForm

app = Flask(__name__)
app.secret_key = 'supersecretkey'

@app.route('/form', methods=['GET', 'POST'])
def form():
    form = MyForm()
    if request.method == 'POST':
        return f"Hello, {form.username.data}!"
    return render_template('form.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
