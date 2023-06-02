from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify



# Create your models here.
class Curso(models.Model):

    nombre=models.CharField(max_length=40)
    camada = models.IntegerField()

    def __str__(self):
        return f"Curso: {self.nombre} - Camada: {self.camada}"


class Estudiante(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()

class Profesor(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()
    profesion= models.CharField(max_length=30)


    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido {self.apellido} - E-Mail {self.email} - Profesión {self.profesion}"

class Entregable(models.Model):
    nombre= models.CharField(max_length=30)
    fechaDeEntrega = models.DateField()  
    entregado = models.BooleanField()



def get_image_filename(instance, filename):
    title =  'titulo'
    slug = slugify(title)
    return "imagenesAvatares/%s-%s" % (slug, filename)  


class Avatar(models.Model):
    #vinvulo con el usuario
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #Subcaperta avatares de media :) 
    imagen = models.ImageField(upload_to='avatares', null=True, blank = True)

    def __str__(self):
        return f"Imagen de: {self.user.username}"

   


