from django.shortcuts import render
from django.utils.translation import gettext_lazy as _
from clients.forms import ClientForm
# Create your views here.


def justice_clients(request):

    context = {
        'active_page': 'clients', 
        }
    template_name = 'clients/index.html'
    return render(request=request, template_name=template_name, context=context)
    
    
def add_client(request):
    
    form_client = ClientForm(request, )
    
    context = {
        'active_page': 'clients', 
        }
    template_name = 'clients/index.html'
    return render(request=request, template_name=template_name, context=context)
