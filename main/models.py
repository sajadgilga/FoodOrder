from uuid import uuid4

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.utils.safestring import mark_safe

# every object model has its foreign key
class Food(models.Model):
    name = models.CharField(max_length=128, default='غذا')  # you must determine what length the fields in database have
    description = models.CharField(max_length=512)
    create_date = models.DateTimeField(auto_now_add=True)
    picture = models.FileField(blank=True, null=True, upload_to='static/food_pics')  # blank is for validation of forms,
    #  null is for making it optional to save it null
    ## another mode of saving models.FilePathField()

    def image_tag(self):
        return mark_safe("<img src='/%s' style='max-width:250px; height=auto'/>" % self.picture)

# we must first run 'makemigration' and 'migrate' to create model in database

class Order(models.Model):
    food = models.ForeignKey(to=Food, on_delete=models.CASCADE)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    date = models.DateTimeField()
    orderID = models.UUIDField(default=uuid4, editable=False, unique=True)
