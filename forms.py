from flask_wtf import FlaskForm
from wtforms import (
    StringField, FloatField, IntegerField,
    SelectField, FieldList, FormField, SubmitField, Form
)
from wtforms.validators import DataRequired, NumberRange, InputRequired

class DrinkForm(Form):
    rodzaj = SelectField("Rodzaj",choices=[("0", "Wybierz"), ("1", "duze piwo"), ("2", "male piwo"), ("3", "wino"), ("4", "ciezki alkohol")])
    czas = IntegerField("Jak dawno temu bylo spozywane [min]", default=0, validators=[InputRequired(), NumberRange(min=0)])

class MainForm(FlaskForm):
    age = IntegerField("Wiek", validators=[DataRequired(), NumberRange(min=1)])
    weight = FloatField("Waga (kg)", validators=[DataRequired(), NumberRange(min=1)])
    height = FloatField("Wzrost (cm)", validators=[DataRequired(), NumberRange(min=1)])
    sex = SelectField("Płeć", choices=[("M", "Mężczyzna"), ("F", "Kobieta")], validators=[DataRequired()])

    lista_drinkow =  FieldList(FormField(DrinkForm), min_entries=10)

    submit = SubmitField("Oblicz")
