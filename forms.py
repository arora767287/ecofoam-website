from flask.ext.wtf import Form, TextField, TextAreaField, SubmitField

class Contacts(Form):
    name = TextField("Name")
    email = TextField("Email")
    subject = TextField("Subject")
    message = TextAreaField("Message")
    submit = SubmitField("Send The Message")
    