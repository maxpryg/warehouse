from django.urls import path

from . import views

app_name = 'trucks'
urlpatterns = [
    path('', views.TruckListView.as_view(), name='trucks'),
    path('<int:pk>/', views.detail, name='detail'),
    path('add/', views.add_truck, name='add-truck'),
    path('<int:pk>/vote/', views.vote, name='vote'),
]
