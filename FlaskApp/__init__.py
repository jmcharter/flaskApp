from flask import Flask, render_template, request
from flask_wtf import Form
from wtforms import StringField, BooleanField, FloatField
from wtforms.validators import DataRequired, NumberRange


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
    paragraph = "How's this for an about page?"
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
        divide_by = FloatField("Divide by", validators=[NumberRange(min=1)])

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


if __name__ == "__main__":
    app.run()
    app.debug = True
