from django.db import models
from present.models import Present
from django import forms
# Create your models here.


class Choice(models.Model):
    poll = models.ForeignKey(Present,on_delete=models.CASCADE) #Poll 모델의 id를 이용

    PRESENT_CHOICES = (
        ('0~10','0~10'),
        ('10~20','10~20'),
        ('20~30','20~30'),
        ('30~40','30~40'),
        ('40~50','40~50'),
        ('50~60','50~60'),
        ('60~','60~'),
    )
    age = models.CharField(
        max_length=10,
        choices=PRESENT_CHOICES,
        default='0~10',
    )
    votes = models.IntegerField(default = 1)

