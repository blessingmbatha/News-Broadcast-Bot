from flask_wtf import FlaskForm
from wtforms import SelectField, BooleanField

class SubscriptionForm(FlaskForm):
    is_subscribed = BooleanField('Yes, subscribe!')
    schedule = SelectField('Scedule', choices=[(8, '08:00'), (12, '12:00'), (21, '21:00')])