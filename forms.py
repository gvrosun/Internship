from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


class StoredForm(FlaskForm):
    name = StringField('Name ', validators=[DataRequired()], render_kw={"placeholder": "Single word name"})
    message = TextAreaField('Message ', validators=[DataRequired()], render_kw={"placeholder": "Your thoughts here", "rows": 8})
    submit = SubmitField("Comment")
