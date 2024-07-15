from django.db import models


# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=30)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Food(models.Model):
    name = models.CharField(max_length=25)
    image = models.CharField(max_length=300)
    description = models.TextField()
    price = models.IntegerField()
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Food'
        verbose_name_plural = 'Foods'


class Chef(models.Model):
    name = models.CharField(max_length=25)
    responsibility = models.CharField(max_length=25)
    description = models.TextField()
    image = models.CharField(max_length=300)
    facebook_ID = models.CharField(max_length=30, blank=True)
    twitter_ID = models.CharField(max_length=30, blank=True)
    instagram_ID = models.CharField(max_length=30, blank=True)
    youtube_ID = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Chef'
        verbose_name_plural = 'Chefs'


class ContactForm(models.Model):
    form_name = models.CharField(max_length=25)
    form_email = models.EmailField()
    form_message = models.TextField()

    def __str__(self):
        return self.form_name

    class Meta:
        verbose_name = 'Contact Form'
        verbose_name_plural = 'Contact Forms'
