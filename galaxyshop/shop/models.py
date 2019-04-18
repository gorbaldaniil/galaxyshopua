from django.db import models

class Product(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    characteristic = models.TextField()
    price = models.CharField(max_length=200)
    photo = models.ImageField(upload_to="shop/static/product")
    reviews = models.TextField()
