from django.db import models

# Create your models here.
class Aplicacion(models.Model):
    nombre =  models.CharField(max_length=50)
    descripcion =  models.CharField(max_length=200)
    linkDescarga =  models.CharField(max_length=300)
    imagen =  models.CharField(max_length=50)
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

