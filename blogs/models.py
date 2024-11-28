from django.db import models

class Category(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class BlogPost(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    content=models.TextField()
    thumbnail=models.ImageField(upload_to="uploads/")
    author=models.CharField(max_length=100)
    published=models.DateTimeField(auto_now=True)
    edited=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

