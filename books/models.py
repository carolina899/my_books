from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=250)
    
    def __str__(self):
        return self.title
    
class Book(models.Model):
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    image = models.ImageField(upload_to='books_images/', blank=True, null=True)
    summary = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
     return self.title