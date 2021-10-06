
from django.views.static import serve
from django.urls import path, include
from affaires import views

urlpatterns = [
    
    path('avocats_charges/',  include([
         # Avocat charge URLs ***************************************
         path('', views.justice_avocats_charges_all,  name='justice_avocats_charges_all'),
         path('page/<int:page>/city/<str:city>/search/<slug:query>', views.justice_avocats_charges, name='justice_avocats_charges'),
         path('create', views.avocat_charge_form, name='avocat_charge_create'),
         path('<int:id>/edit', views.avocat_charge_form,name='avocat_charge_update'),
         path('<int:id>/delete', views.avocat_charge_delete, name='avocat_charge_delete'),
         ])),

]
