from django.db import models 
 
#pipenv run python manage.py makemigrations (activar los modelos)

# Create your models here.
class Post(models.Model):
    """ descripcion de mi clase """
    title = models.CharField(max_length=200)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)  