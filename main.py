from flask import Flask, render_template, request, flash
from flask_wtf import Form
from wtforms import TextField, TextAreaField,SubmitField, validators, ValidationError
from flask_mail import Message, Mail
import smtplib

class Contacts(Form):
    name = TextField("Name", [validators.Required()])
    email = TextField("Email", [validators.Required(), validators.Email()])
    subject = TextField("Subject", [validators.Required()])
    message = TextAreaField("Message", [validators.Required()])
    submit = SubmitField("Submit")
    

app = Flask(__name__)
mail = Mail()

app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = 'teamecofoam@gmail.com'
app.config["MAIL_PASSWORD"] = 'ecofoco1956'


mail.init_app(app)

app.secret_key = 'ECOFOAM2021'

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")
@app.route("/our-journey")
def journey():
    return render_template("journey.html") 
@app.route("/mission") 
def mission():
    return render_template("mission.html")
@app.route("/products")   
def products():
    return render_template("products.html")
@app.route("/contact", methods=["GET", "POST"])
def contact():
    form = Contacts()
    if request.method == 'POST':
        if form.validate == False:
            flash("Some fields are empty")
            return render_template("contact.html", form=form)
        else:
            msg = Message(form.subject.data, sender="teamecofoam@gmail.com", recipients=[email.form.data, "teamecofoam@gmail.com"]) #Change Settings In Email To Make Them Less Secure
            msg.body = """
            From: %s <%s>
            %s
            """ % (form.name.data, form.email.data, form.message.data)
            mail.send(msg)
 
            return "Form Sent" #Change Default Message Based On If-Else Statement
    elif request.method == "GET":
        return render_template("contact.html", form=form)  


if __name__ == "__main__":
    app.run(debug=True)
