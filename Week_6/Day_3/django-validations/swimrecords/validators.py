import re
from django.core.exceptions import ValidationError
from django.utils import timezone

def name_validator(name):
    pattern = r"[^A-Za-z]"
    matches = re.search(pattern, name)

    if matches or name == '':
        raise ValidationError("Name must be letters only and can't be blank")

def stroke_validator(stroke):
    strokes = ['front crawl', 'butterfly', 'breast', 'back', 'freestyle']

    if not stroke in strokes:
        raise ValidationError(stroke + " is not a valid stroke")

def distance_validator(distance):
    if distance < 50:
        raise ValidationError('Ensure this value is greater than or equal to 50.')

def date_validator(date):
    current_date = timezone.now()
    if current_date < date:
        raise ValidationError("Can't set record in the future.")
    
def broken_record_validator(date):
    current_date = timezone.now()
    if current_date > date:
        raise ValidationError("Can't break record before record was set.")