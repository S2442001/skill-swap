from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length

class SkillForm(FlaskForm):
    name = StringField("Skill Name", validators=[DataRequired(), Length(min=2, max=64)])
    type = SelectField(
        "Type",
        choices=[("offered", "Offered"), ("requested", "Requested")],
        validators=[DataRequired()],
    )
    submit = SubmitField("Add Skill")
