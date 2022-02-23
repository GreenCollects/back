from django.db import models
from django.contrib.auth.models import User

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
    collect = models.ManyToManyField(Waste)

class Rating(models.Model):
    point = models.ForeignKey(Point, on_delete=models.CASCADE, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)

    class Meta:
       unique_together = ("point", "user")

class CommunityCollect(models.Model):
    collectDate = models.DateTimeField(null=False, blank=False)
    quantityMax = models.FloatField(blank=False)
    collectPoint = models.ForeignKey(Point, on_delete=models.CASCADE, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)

class Participation(models.Model):
    waste = models.ForeignKey(Waste, on_delete=models.CASCADE, null=False)
    collect = models.ForeignKey(CommunityCollect, on_delete=models.CASCADE, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)

    class Meta:
       unique_together = ("waste", "collect", "user")