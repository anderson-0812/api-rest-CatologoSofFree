from django.contrib import admin
from .models import Aplicacion, Licencia


# Register your models here.
class LicenciaInline(admin.StackedInline):
		model  = Licencia
		extra = 1

class AplicacionAdmin(admin.ModelAdmin):
    list_display = ['nombre','descripcion']
    inlines =[LicenciaInline]

admin.site.register(Aplicacion,AplicacionAdmin)
admin.site.register(Licencia)
