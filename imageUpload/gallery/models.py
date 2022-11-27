from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
class Photo(models.Model):
    uploader = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length= 500)
    created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='photos/')
    
    def __str__(self) -> str:
        return str(self.title)