
from django.views.static import serve
from django.urls import path, include
from justice import views

urlpatterns = [
    path('', views.index, name='home'),
    path('', include('clients.urls')),
    path('', include('adversaires.urls')),
]
