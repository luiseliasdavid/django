from django.db import models 
 
#pipenv run python manage.py makemigrations (activar los modelos)

# Create your models here.
class Post(models.Model):
    """ descripcion de mi clase """
    title = models.CharField(max_length=200, verbose_name="titulo")
    content = models.TextField(verbose_name="Contenido")
    created = models.DateTimeField(auto_now_add=True,verbose_name="Creado")
    modified = models.DateTimeField(auto_now=True,verbose_name="Modificado")  
    
    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name= "Entrada"
        verbose_name_plural="entradas"

