from django.db import models

#Lenguajes
lenguaje_aplicacion = [
    (1,'Java'),
    (2,'Python'),
    (3,'Javascript'),
    (4,'Php'),
    (5,'C#'),
    (6,'C++'),
    (7,'Otros'),
]

#Categorias
categoria_aplicacion = [
    (1,'Ofimatica'),
    (2,'Video'),
    (3,'Audio'),
    (4,'Programacion'),
    (5,'Música'),
    (6,'Mantenimiento Computadores'),
    (7,'Otros'),
]

# Create your models here.
class Aplicacion(models.Model):
    nombre =  models.CharField(max_length=50)
    descripcion =  models.CharField(max_length=200)
    linkDescarga =  models.CharField(max_length=300)
    imagen =  models.CharField(max_length=50)
    versionApp =  models.CharField(max_length=50)
    fechaCreacion = models.DateTimeField(auto_now_add=True)
    # Lenguajes app
    lenguaje = models.IntegerField(
        null=False, blank=False,
        choices=lenguaje_aplicacion,
        default= 1
    )
    # Categorias app
    categoria = models.IntegerField(
        null=False, blank=False,
        choices=categoria_aplicacion,
        default= 1
    )

    # licencias = models.ForeignKey(Licencia,on_delete = models.CASCADE, null = False, blank= False)

    # address =  models.CharField(max_length=100)
    def __str__(self):
        return '{}'.format(self.nombre)


class Licencia(models.Model):
    nombre =  models.CharField(max_length=50)
    tipoLicencia =  models.CharField(max_length=200)
    costoLicencia =  models.CharField(max_length=300)
    aplicaciones =  models.ForeignKey(Aplicacion, on_delete = models.CASCADE
    , related_name='aplicaciones') #model_set
    # imagen =  models.CharField(max_length=50)
    # address =  models.CharField(max_length=100)
    def __str__(self):
        return '{} {} {} {}'.format(self.nombre, self.tipoLicencia
        , self.costoLicencia, self.aplicaciones)

