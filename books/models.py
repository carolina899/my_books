from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=250)
    
    def __str__(self):
        return self.title
    
class Book(models.Model):
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    image = models.CharField(max_length=2000)
    created_at =models.CharField(auto_now_add=True)
    update_at = models.CharField(auto_now=True)

    def __str__(self):
        return self.title
    
    category = models.ForeignKey(Category, related_name='book', on_delete=models.CASCADE)