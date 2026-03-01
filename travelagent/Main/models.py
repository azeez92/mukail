from django.db import models
from django.utils.text import slugify

# Create your models here.
class Destination(models.Model):
    title=models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    location =models.CharField(max_length=200)
    image = models.ImageField(upload_to='destinations/')
    price= models.DecimalField(max_digits=10, decimal_places=2)
    showers= models.IntegerField(default=0)
    days= models.IntegerField()
    beds = models.IntegerField(default=0)
    feature =models.CharField(max_length=100)
    description= models.TextField()


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*arg, **kwargs)

    def __str__(self):
        return self.titl