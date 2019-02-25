from django.db import models

class Present(models.Model):
    title = models.CharField(max_length =200)
    category = models.CharField(max_length =200)
    image = models.ImageField()
    price = models.IntegerField()
    
    def __str__(self):
        return self.title