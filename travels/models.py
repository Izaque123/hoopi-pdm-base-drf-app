from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.utils import timezone

# Create your models here.

class Travel(models.Model):
    id = models.AutoField(primary_key=True)
    start = models.CharField(max_length=100)
    end = models.CharField(max_length=100)
    start_date = models.DateField()
    time = models.TimeField()
    places = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    passenger_list = models.ManyToManyField(User, related_name='travels', blank=True)
    create_by = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True, null=True)


    def __str__(self):
        return f"Travel of {self.start} to {self.end} on {self.start_date} at {self.time} with {self.places} places for ${self.price}"