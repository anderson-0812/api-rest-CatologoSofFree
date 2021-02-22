
from django.urls import path, include


from .views import AplicacionListView, LicenciaListView

urlpatterns = [
    path('aplicacion/', AplicacionListView.as_view(), name='aplicacion_list'),
    path('licencia/', LicenciaListView.as_view(), name='licencia_list'),
    # path('user/<int:pk>/', UserDetailtView.as_view(), name='user_detail'),
]
