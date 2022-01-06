""" Posts models"""

# Django
from django.db import models

# Models
from django.contrib.auth.models import User

class Post(models.Model):
    """Post model"""
    
      ## Para relacionar el post con un usuario utilizamos ForeignKey
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    ## Traemos el modelo de otra manera con un string representando la ruta app/modelo
    profile = models.ForeignKey('users.Profile', on_delete=models.CASCADE)
    
    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='post/photos')
    
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.title} by @{self.user.username}'