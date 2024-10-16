from flask_wtf import FlaskForm
from wtforms import  TextAreaField ,SubmitField
from wtforms.validators import DataRequired


class Sentiment_Analyze(FlaskForm):
    text = TextAreaField("Enter your Comment",validators=[DataRequired()], render_kw={'rows':10,'cols':50})
    submit = SubmitField("Analyze")