from django.urls import path

from . import views

app_name = 'trucks'
urlpatterns = [
    path('', views.TruckListView.as_view(), name='trucks'),
    path('<int:pk>/', views.truck_detail, name='truck-detail'),
    path('add/', views.add_truck, name='add-truck'),
    path('<int:pk>/<hu>/', views.handling_unit_detail,
        name='handling-unit-detail'),
]
