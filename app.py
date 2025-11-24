from flask import Flask, render_template, redirect, url_for, flash
from forms import MainForm
from logic import calculate_can_drive

app = Flask(__name__)
app.secret_key = "foo"


@app.route("/", methods=["GET", "POST"])
def index():
    form = MainForm()
    if form.validate_on_submit():
        # Access data from the form
        age = form.age.data
        weight = form.weight.data
        height = form.height.data
        sex = form.sex.data
        drinks = [
            {"rodzaj": drink.rodzaj.data, "czas": drink.czas.data}
            for drink in form.lista_drinkow
        ]
        gramy_alkocholu = calculate_can_drive(drinks)
        
        # For demonstration, just flash the submitted data
        # flash(f"Wiek: {age}, Waga: {weight}, Wzrost: {height}, Płeć: {sex}")
        # flash(f"Lista drinków: {drinks}")
        flash(f"Ilosc gram alhocholu to: {gramy_alkocholu}")
        
        return redirect(url_for("index"))

    return render_template("index.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)
