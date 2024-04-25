from django.db import models

class UserProfile(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female')])
    username = models.CharField(max_length=200, unique=True)
    password = models.CharField(max_length=200)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)

    class Meta:
        db_table = "details"

from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='item_images/')
    store = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Restaurant_data'
