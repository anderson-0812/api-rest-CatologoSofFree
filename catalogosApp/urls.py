
from django.urls import path, include


from .views import AplicacionListView, LicenciaListView, AplicacionDetailtView, LicenciaDetailtView

urlpatterns = [
    path('aplicacion/', AplicacionListView.as_view(), name='aplicacion_list'),
    path('aplicacion/<int:pk>/', AplicacionDetailtView.as_view(), name='aplicacion_detail'),

    path('licencia/', LicenciaListView.as_view(), name='licencia_list'),
    path('licencia/<int:pk>/', LicenciaDetailtView.as_view(), name='lincencia_detail'),
]
