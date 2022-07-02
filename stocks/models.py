
from statistics import mode
import uuid
from xml.parsers.expat import model
from django.db import models
from users.models import User

# Create your models here.
class Stock(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey('users.User', related_name='owned_stocks', on_delete=models.CASCADE) # represent the user who created the code snippet
    stock_symbol = models.CharField(max_length=256, blank=False)
    stock_name = models.CharField(max_length=256, blank=False)
    share_number = models.IntegerField(blank=False)
    purchase_price = models.DecimalField(max_digits=20, decimal_places=2, blank=False)
    purchase_time = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['created']
    # def __str__(self):
    #     return f"owner:{self.owner}, stock_symbol:{self.stock_symbol}, stock_name:{self.stock_name} , share_number:{self.share_number}, purchase_price:{self.purchase_price}, purchase_time:{self.purchase_time}"
