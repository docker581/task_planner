from flask_wtf import FlaskForm
from wtforms import StringField, DateField
from wtforms.validators import InputRequired


class TaskForm(FlaskForm):
    title = StringField('Заголовок', validators=[InputRequired()])
    description = StringField('Описание', validators=[InputRequired()])
    date = DateField('Дата', validators=[InputRequired()])
