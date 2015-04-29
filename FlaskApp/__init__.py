# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
from flask_wtf import Form
from wtforms import StringField, BooleanField, FloatField
from wtforms.validators import DataRequired, NumberRange
from retireapp import *


app = Flask(__name__)
app.config['SECRET_KEY'] = 'lskhjagdfl;sahjkgd'


@app.route("/")
def test():

    title = "FlaskApp"
    paragraph = "Welcome to this Flask Application"
    activePage = "index"

    return render_template(
        "index.html", paragraph=paragraph, title=title, activePage=activePage)


@app.route("/about")
def about():

    title = "About"
    paragraph = "Flask based Retirement Calculator." u"©" "2015 Jon Charter"
    activePage = "about"

    return render_template(
        "index.html", paragraph=paragraph, title=title, activePage=activePage)


@app.route("/contact")
def contact():

    title = "Contact"
    paragraph = "How's this for a contact page?"
    activePage = "contact"

    return render_template(
        "index.html", paragraph=paragraph, title=title, activePage=activePage)


@app.route("/form", methods=['GET', 'POST'])
def form():

    pageType = "form"
    title = "Form"
    paragraph = "How's this for a form?"
    activePage = "form"

    class DivideForm(Form):
        number = FloatField("Number")
        divide_by = FloatField(
            "Divide by",
            validators=[NumberRange(
                min=1,
                message="Please only enter numbers. \
                Number must be greater than 1.")])

    form = DivideForm()
    result = None

    if form.validate_on_submit():
        result = form.number.data / form.divide_by.data

    return render_template(
        "divide.html",
        paragraph=paragraph,
        title=title,
        pageType=pageType,
        activePage=activePage,
        result=result,
        form=form)


@app.route("/app", methods=['GET', 'POST'])
def retire():
    pageType = "app"
    title = "Retirement Calculator"
    paragraph = "The retirement calculator!"
    activePage = "app"

    class RetirementCalculator(Form):
        income = FloatField("What is your annual income?")
        housecost = FloatField("How much does your rent cost per month?")
        bills = FloatField("How much do your bills cost each month?")
        uage = FloatField("How old are you?")
        rage = FloatField("At what age do you plan to retire?")
        pension = FloatField("How much do you currently have saved towards "
                             "retirement? (Including pension)")

    app = RetirementCalculator()
    result = None

    if app.validate_on_submit():
        calculation = RetireApp(
            app.income.data,
            app.housecost.data,
            app.bills.data,
            app.uage.data,
            app.rage.data,
            app.pension.data
        )
        calculation.Calculate()
        result = calculation.Statement()

    return render_template(
        "retire.html",
        paragraph=paragraph,
        title=title,
        pageType=pageType,
        activePage=activePage,
        result=result,
        app=app)


if __name__ == "__main__":
    app.run()
    app.debug = True
