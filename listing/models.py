from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.conf import settings

from django.contrib.auth.models import AbstractUser
from django.db import models
User = get_user_model()
# class CustomUser(AbstractUser):
#     pass
#     # add additional fields in here

#     def __str__(self):
#         return self.username

class Post(models.Model):
    title = models.CharField(max_length=100, help_text="Enter Title")
    description = models.TextField(help_text="Please describe your listing")
    bedroom = models.CharField(max_length=150, null=True)
    city = models.CharField(max_length=100, null=True)
    price = models.DecimalField(max_digits=6,decimal_places=2)
    #picture = models.ImageField()
    pub_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
   
    slug = models.SlugField()

    class Meta:
        ordering = ['title', '-pub_date']
    
    def get_absolute_url(self):
        return reverse("detail", kwargs={
            'slug': self.slug
        })
 
    
    def get_all_books(self):
        return self.Post.all()
    def price_under_onek(self):
        if self.price < 1000.00:
            return self.Post.price.all()
        else:
            return str('Sorry none')

    def __str__(self):
        return self.title



