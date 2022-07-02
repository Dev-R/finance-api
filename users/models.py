from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    created = models.DateTimeField(auto_now_add=True)
    cash = models.DecimalField(default=10000, decimal_places=2, max_digits=19)
    email = models.EmailField(max_length=100, blank=False)
    image = models.ImageField(upload_to="blog/%Y/%m/%d", null=True)
    # Image_link = models.URLField(blank=True)
    class Meta:
        ordering = ['created']



