from wtforms.validators import DataRequired, Email
from wtforms import StringField, TextAreaField
from flask_wtf import FlaskForm

class CommentForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    username = StringField('Username')
    text = TextAreaField('Comment', validators=[DataRequired()])
