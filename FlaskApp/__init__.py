from flask import Flask, render_template, request
from flask_wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.debug = True


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
    result = None

    if request.method == 'POST':
        number = float(request.form['number'])
        divide_by = float(request.form['divide_by'])
        result = number / divide_by

    return render_template(
        "divide.html",
        paragraph=paragraph,
        title=title,
        pageType=pageType,
        activePage=activePage,
        result=result)


if __name__ == "__main__":
    app.run()
