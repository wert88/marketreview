from django.db import models
from django.shortcuts import render, reverse
from django.conf import settings
from django import forms


CATEGORY_CHOICES = (
    ('S', 'Sports'),
    ('H', 'Health & Beauty'),
    ('B', 'Books'),
	('MF', 'Men Fashion'),
	('SW', 'Software'),
	('K', 'Kids & Babies'),
	('E', 'Electronics'),
)

LABEL_CHOICES = (
	('A', ''),
    ('P', 'primary'),
    ('S', 'secondary'),
    ('D', 'danger')
)

ADDRESS_CHOICES = (
    ('B', 'Billing'),
    ('S', 'Shipping'),
)

class BannerImg(models.Model):
	title = models.CharField(max_length=100)
	bannerimage = models.ImageField()
	
	def __str__(self):
		return self.title


class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    label = models.CharField(choices=LABEL_CHOICES, max_length=1,)
    slug = models.SlugField(unique=True)
    intro_description = models.TextField()
    description = models.CharField(max_length=225)
    callout = models.CharField(max_length=400)
    extra_description = models.TextField()
    image = models.ImageField()
    image2 = models.ImageField(default="blank")
    image3 = models.ImageField(default="blank")
    image4 = models.ImageField(default="blank")
    Buy_url = models.TextField(default='#')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
       return reverse("app:product", kwargs = {'slug': self.slug})
	   
	   
class ContactModel(models.Model):
    from_email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.TextField()
    time = models.DateTimeField(auto_now=True)
	
    def __str__(self):
        return '(Email : ) ' + self.from_email + ' (Subject : ) ' + self.subject + ' ( Time : ) ' + str(self.time) + ' ( Message : ) ' + self.message 
