"""User models"""

#Django
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    """Profile model.
    
    Proxy model that extends the base data with other information
    """
    
    ## Cascade lo que hace es definir que va a pasar cuando se elimine su modelo de dependencia
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    website = models.URLField(max_length=200, blank=True)
    biography = models.TextField(blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    
    ## Django no guarda la media en la DB, guarda una referencia
    ## Requiere libreria pill
    picture = models.ImageField(upload_to='users/pictures', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.user.username
    
