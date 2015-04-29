# -*- coding: utf-8 -*-

# Imports: Flask, WTForms, Retirement Calculations Script

from flask import Flask, render_template, request
from flask_wtf import Form
from wtforms import StringField, BooleanField, FloatField
from wtforms.validators import DataRequired, NumberRange
from retireapp import *

# Initiate Flask
app = Flask(__name__)

# Set the secret key. This is a bad way to do so,
# in a live application this would be hidden and
# not placed within the __init__ file.
app.config['SECRET_KEY'] = 'lskhjagdfl;sahjkgd'


# Define Index page, followed by content pages
# Set parameters, then push them into template
@app.route("/")
def test():

    title = "FlaskApp"
    paragraph = "Welcome to this Flask Application"
    activePage = "index"

    return render_template(
        # "page to render template", 
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
    paragraph = "For contact please write to: jon@joncharter.co.uk"
    activePage = "contact"

    return render_template(
        "index.html", paragraph=paragraph, title=title, activePage=activePage)


# Uses methods GET and POST for taking user input into the calculator
@app.route("/division", methods=['GET', 'POST'])
def division():

    pageType = "division"
    title = "Division"
    paragraph = "Enter any two numbers to calculate a division"
    activePage = "division"

    class DivideForm(Form):
        number = FloatField("Number")
        divide_by = FloatField(
            "Divide by",
            validators=[NumberRange(  # Defines what input is valid
                min=1,
                message="Please only enter numbers. \
                Number must be greater than 1.")])

    divform = DivideForm()
    result = None

    # If input is valid, run the calculation
    if divform.validate_on_submit():
        result = divform.number.data / divform.divide_by.data

    return render_template(
        "divide.html",
        paragraph=paragraph,
        title=title,
        pageType=pageType,
        activePage=activePage,
        result=result,
        form=divform)


@app.route("/app", methods=['GET', 'POST'])
def retire():
    pageType = "app"
    title = "Retirement Calculator"
    paragraph = "The retirement calculator!"
    activePage = "app"

    # Class for calculator. Takes input from form.
    class RetirementCalculator(Form):
        income = FloatField("What is your annual income?")
        housecost = FloatField("How much does your rent cost per month?")
        bills = FloatField("How much do your bills cost each month?")
        uage = FloatField("How old are you?")
        rage = FloatField("At what age do you plan to retire?")
        pension = FloatField("How much do you currently have saved towards "
                             "retirement? (Including pension)")

    # Create an instance of the class RetirementCalculator
    app = RetirementCalculator()
    result = None

    # Validate all input, then run app with forms input
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
