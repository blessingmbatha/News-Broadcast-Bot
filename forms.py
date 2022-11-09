from flask_wtf import FlaskForm
from wtforms import SelectField, BooleanField

class SubscriptionForm(FlaskForm):
    is_subscribed = BooleanField('Yes, subscribe!')
    schedule = SelectField('Scedule', choices=[(8, '08:00'), (9, '09:00'), (10, '10:00'), (11, '11:00'), (12, '12:00'), (13, '13:00'), (14, '14:00'), (15, '15:00'), (16, '16:00'), (17, '17:00'), (18, '18:00'), (19, '19:00'), (20, '20:00'), (21, '21:00')])