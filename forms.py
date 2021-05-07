from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


class StoredForm(FlaskForm):
    name = StringField('Name: ', validators=[DataRequired()], render_kw={"placeholder": "Name"})
    message = TextAreaField('Message: ', validators=[DataRequired()], render_kw={"placeholder": "Message", "rows": 8})
    submit = SubmitField("Comment")
