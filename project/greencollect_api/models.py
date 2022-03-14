from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Waste(models.Model):
    label = models.CharField(max_length=30, unique=True, blank=False)
    creationDate = models.DateTimeField(auto_now_add=True)
    updateDate = models.DateTimeField(auto_now=True)

class Preventive(models.Model):
    data = models.TextField(max_length=1000, blank=False)
    creationDate = models.DateTimeField(auto_now_add=True)
    updateDate = models.DateTimeField(auto_now=True)
    activated = models.BooleanField(default=True)
    linkedWaste = models.ForeignKey(Waste, on_delete=models.CASCADE, null=False)

class Point(models.Model):
    label = models.CharField(max_length=30, unique=True, blank=False)
    creationDate = models.DateTimeField(auto_now_add=True)
    updateDate = models.DateTimeField(auto_now=True)
    activated = models.BooleanField(default=True)
    wastes = models.ManyToManyField(Waste, related_name="wastes_for_point")
    latitude = models.FloatField(default=0.0, validators=[MinValueValidator(-90), MaxValueValidator(90)])
    longitude = models.FloatField(default=0.0, validators=[MinValueValidator(-180), MaxValueValidator(180)]) 
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, default=1) 

class Rating(models.Model):
    point = models.ForeignKey(Point, on_delete=models.CASCADE, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    creationDate = models.DateTimeField(auto_now_add=True)
    updateDate = models.DateTimeField(auto_now=True)
    rate = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(10)])
    
    class Meta:
       unique_together = ("point", "user")

class CommunityCollect(models.Model):
    collectDate = models.DateTimeField(null=False, blank=False)
    quantityMax = models.FloatField(blank=False)
    wastes = models.ManyToManyField(Waste, related_name="wastes_for_community_collect")
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    creationDate = models.DateTimeField(auto_now_add=True)
    updateDate = models.DateTimeField(auto_now=True)
    latitude = models.FloatField(default=0.0, validators=[MinValueValidator(-90), MaxValueValidator(90)])
    longitude = models.FloatField(default=0.0, validators=[MinValueValidator(-180), MaxValueValidator(180)]) 

class Participation(models.Model):
    waste = models.ForeignKey(Waste, on_delete=models.CASCADE, null=False)
    collect = models.ForeignKey(CommunityCollect, on_delete=models.CASCADE, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    creationDate = models.DateTimeField(auto_now_add=True)
    updateDate = models.DateTimeField(auto_now=True)

    class Meta:
       unique_together = ("waste", "collect", "user")