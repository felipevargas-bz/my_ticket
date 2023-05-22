from django.urls import path
from locations import views


urlpatterns = [
    path('api/location/', views.LocationView.as_view(), name='locations'),
    path('api/location/<int:pk>/', views.LocationView.as_view(), name='location'),
    path('api/city/', views.CityView.as_view(), name='cities'),
    path('api/city/<int:pk>/', views.CityView.as_view(), name='city'),
    path('api/departament/', views.DepartmentView.as_view(), name='departaments'),
    path('api/departament/<int:pk>/', views.DepartmentView.as_view(), name='departament'),
    path('api/country/', views.CountryView.as_view(), name='countries'),
    path('api/country/<int:pk>/', views.CountryView.as_view(), name='country'),
]
