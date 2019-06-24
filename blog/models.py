from django.db import models
from django.urls import reverse
from datetime import date
from django.urls import reverse 
from django.contrib.auth.models import User

class Tag (models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Blog (models.Model):
    title = models.CharField(max_length=300)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    category = models.ManyToManyField(Tag)
    date = models.DateField(null=True, blank=True)
    description = models.TextField(max_length=5000)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-date"]

    def get_absolute_url(self):
        return reverse('blog-detail', args=[str(self.id)])

    def categories(self):
        return ', '.join(category.name for category in self.category.all())
    
    categories.short_description = 'Tag'
   

class Author (models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    bio = models.TextField(max_length=300, help_text="Enter your bio here.", null=True)

    class Meta:
        ordering = ["user","bio"]

    def get_absolute_url(self):
        return reverse('author-bio', args=[str(self.id)])

    def __str__(self):
        return self.name

class Comment (models.Model):
    description = models.TextField(max_length=500, help_text="Enter comment about blog here.", default="")
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now_add=True, null=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ["date"]

    


