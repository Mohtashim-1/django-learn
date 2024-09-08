from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

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
    description = models.TextField(default='')

    def __str__(self):
        return self.name

# ONE TO MANY
class ChaiReview(models.Model):
    chai = models.ForeignKey(ChaiVariety, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    date_added = models.TimeField(default=timezone.now)

    def __str__(self):
        return f'{self.user } has been reviews for {self.chai.name}'
    
# MANY TO MANY

class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    ChaiVariety = models.ManyToManyField(ChaiVariety, related_name='store')

    def __str__(self):
        return self.name

# ONE TO ONE 

class ChaiCertificate(models.Model):
    chai = models.OneToOneField(ChaiVariety, on_delete=models.CASCADE, related_name='certificate')
    certificate_number = models.CharField(max_length=100)
    issue_date = models.DateTimeField(default=timezone.now)
    valid_until = models.DateTimeField()

    def __str__(self):
        return f"Certificate for {self.chai} - {self.name.chai}"