from django.db import models
from .validators import *

class SwimRecord(models.Model):
    first_name = models.CharField(max_length=250, validators=[name_validator])
    last_name = models.CharField(max_length=250, validators=[name_validator])
    team_name = models.CharField(max_length=250, validators=[name_validator])
    relay = models.BooleanField()
    stroke = models.CharField(max_length=250, validators=[stroke_validator])
    distance = models.IntegerField(validators=[distance_validator])
    record_date = models.DateTimeField(validators=[date_validator])
    record_broken_date = models.DateTimeField(validators=[broken_record_validator])