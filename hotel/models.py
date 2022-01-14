from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=30, unique=True)
    slug = models.SlugField(max_length=30, primary_key=True)

    def __str__(self):
        return self.name


class Hotel(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.RESTRICT, related_name='hotels')

    image = models.ImageField(upload_to='hotel', null=True, blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Comment(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    rating = models.SmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    created_at = models.DateField(auto_now_add=True)


class Like(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='likes')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    like = models.SmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(1)])


class Favorite(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='favorites')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorites')
    favorite = models.CharField(max_length=9, null=True, blank=True)


class Cart(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='cart')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cart')
    cart = models.CharField(max_length=19, null=True, blank=True)
