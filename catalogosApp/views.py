
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
        print(JsonResponse(model_to_dict(aplicacionDetail), safe = False))
        return JsonResponse(model_to_dict(aplicacionDetail), safe = False)


class LicenciaListView(View):
    def get(self, request):
        uList = Licencia.objects.all()
        return JsonResponse(list(uList.values()), safe = False)

class LicenciaDetailtView(View):
    def get(self, request, pk):
        licenciaDetail = Licencia.objects.get(pk=pk)
        print(JsonResponse(model_to_dict(licenciaDetail), safe = False))
        return JsonResponse(model_to_dict(licenciaDetail), safe = False)