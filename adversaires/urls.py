
from django.views.static import serve
from django.urls import path, include
from adversaires import views

urlpatterns = [
    path('adversaires/',  include([
         # path('', views.justice_adversaires_all, name='justice_adversaires_all'),
         path('', views.justice_adversaires, name='justice_adversaires'),
         path('create', views.adversaire_form, name='adversaire_create'),
         path('<int:id>/edit', views.adversaire_form, name='adversaire_update'),
         path('<int:id>/delete', views.adversaire_delete, name='adversaire_delete'),
    ])),
    
    
    path('avocats_adversaires/',  include([
         # Avocat Adversaire URLs ***************************************
         # path('', views.justice_avocats_adversaires_all,  name='justice_avocats_adversaires_all'),
         path('',views.justice_avocats_adversaires, name='justice_avocats_adversaires'),
         path('create', views.avocat_adversaire_form, name='avocat_adversaire_create'),
         path('<int:id>/edit', views.avocat_adversaire_form,
              name='avocat_adversaire_update'),
         path('<int:id>/delete', views.avocat_adversaire_delete, name='avocat_adversaire_delete'),
         ])),

]
