
from django.shortcuts import render
from django.views import View
from .models import Aplicacion, Licencia

from django.http import JsonResponse

from django.forms.models import model_to_dict


class AplicacionListView(View):
    def get(self, request):
        uList = Aplicacion.objects.all()
        return JsonResponse(list(uList.values()), safe = False)

class AplicacionDetailtView(View):
    def get(self, request, pk):
        aplicacionDetail = Aplicacion.objects.get(pk=pk)
        licenciasApp = aplicacionDetail.aplicaciones.all()
        diccionarioLicencia = dict()
        arrayLicencia = []
        diccionarioAplicacion = model_to_dict(aplicacionDetail)

        for licens in licenciasApp:
            print(licens)
            diccionarioLicencia['id'] = licens.id
            diccionarioLicencia['nombre'] = licens.nombre
            diccionarioLicencia['tipoLicencia'] = licens.tipoLicencia
            diccionarioLicencia['costoLicencia'] = licens.costoLicencia
            # ESTA OPCION EVITA NO SE ACTIVA DAÑA LA CONSULTA
            # diccionarioLicencia['aplicaciones'] = licens.aplicaciones
            arrayLicencia.append(diccionarioLicencia)

        # print(arrayLicencia)

        # print('aplicacionDetail')
        # print(diccionarioAplicacion)
        diccionarioAplicacion['licencias'] = list(arrayLicencia)
        # print('diccionarioAplicacion')
        # print(diccionarioAplicacion)
        return JsonResponse(diccionarioAplicacion, safe = False)


class LicenciaListView(View):
    def get(self, request):
        uList = Licencia.objects.all()
        return JsonResponse(list(uList.values()), safe = False)

class LicenciaDetailtView(View):
    def get(self, request, pk):
        licenciaDetail = Licencia.objects.get(pk=pk)
        print(JsonResponse(model_to_dict(licenciaDetail), safe = False))
        return JsonResponse(model_to_dict(licenciaDetail), safe = False)