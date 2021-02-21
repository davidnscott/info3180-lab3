from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField
from wtforms.validators import DataRequired, Length, Email

class ContactForm(FlaskForm):
	name = StringField('Name',[DataRequired()])
	email = StringField('Email',[DataRequired(),Email()])
	subject = StringField('Subject',[DataRequired()])
	body = TextField('Message',[DataRequired()])
	submit = SubmitField('Submit')