from flask import Flask, render_template
from forms import MyForm

app = Flask(__name__)
app.secret_key = "supersecterkey"


@app.route('/form', methods=['GET', 'POST'])
def form():
    form = MyForm()
    if form.validate_on_submit():
        return f"Hello, {form.name.data}!"
    return render_template("form.html", form=form)


if __name__ == '__main__':
    app.run(debug=True)
