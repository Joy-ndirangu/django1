from django.db import models

#for user accounts and authentication:
from django.contrib.auth.models import AbstractUser


# Create your models here.

class Students(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    email = models.EmailField(blank=False)
    phone = models.IntegerField()
    image = models.ImageField(upload_to="uploads/images", default="uploads/images/profile.jpg")

    def __str__(self):
        return self.name


class Sliders(models.Model):
    text = models.CharField(max_length=100, blank=False, null=False)
    text1 = models.CharField(max_length=100, blank=False, null=False)
    image = models.ImageField(upload_to="uploads/sliders", default="uploads/sliders/profile.jpg")

    def __str__(self):
        return self.text



#custom class for user registration
#A
class CustomUser(AbstractUser):
    year = models.PositiveIntegerField(blank=True, null=True)






# any minute you modify the models file you must make and run migrations
# python manage.py makemigrations: make migrations - creates the table(model) in database
# python manage.py migrate: running migrations - updates the table/model
