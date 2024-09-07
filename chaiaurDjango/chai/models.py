from django.db import models
from django.utils import timezone
# Create your models here.

class ChaiVariety(models.Model):
    CHAI_TYPE_CHOICE = [
        ('ML','MASLA'),
        ('GR', 'GINGER'),
        ('KL', 'KIWI'),
        ('PL','PLAIN'),
        ('EL', 'ELAICHI')
    ]
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='chais/')
    date_added = models.DateTimeField(default=timezone.now)
    types = models.CharField(max_length=2, choices=CHAI_TYPE_CHOICE)