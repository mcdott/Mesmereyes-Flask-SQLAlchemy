from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, DateField, SelectField, SubmitField, TextAreaField
from wtforms.ext.sqlalchemy.fields import QuerySelectField, QuerySelectMultipleField
from wtforms.validators import DataRequired, Length, ValidationError
from mesmereyes_app.models import InterActivity, Level

class InterActivityForm(FlaskForm):
    """Form to add a new interActivity."""
    title = StringField('Sketch Title',
        validators=[DataRequired(), Length(min=1, max=80)])
    # TODO check if url is valid
    url = StringField('Embed Sketch URL',
        validators=[DataRequired()])
    cc_attribution = TextAreaField('CC Attribution',
        validators=[DataRequired()])
    visual_complexity = SelectField('Visual Complexity', choices=Level.choices())
    visual_contrast = SelectField('Visual Contrast', choices=Level.choices())
    submit = SubmitField('Submit')