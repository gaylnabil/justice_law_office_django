from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.utils.translation import gettext_lazy as _
from clients.forms import ClientForm
from django.urls import reverse

# Create your views here.

def justice_clients(request):

    value = _('list des client')
    context = {
        'title': value,
        'active_page': 'clients',
        'breadcrumb': value,
    }
    template_name = 'clients/index.html'
     
    return render(request=request, template_name=template_name, context=context)
    
    
def client_form(request):
    
    form = ClientForm(request.POST or None)
    
    if request.method == 'POST':
    
        if form.is_valid():
            user = form.save(commit=True)
            # user = form.save()
            redirect_to = reverse('justice_clients')
                                  
            return HttpResponseRedirect(redirect_to)

    value = _('Inscription de client')
    context = {
        'title': value,
        'active_page': 'clients',
        'breadcrumb': value,
        'form': form,
    }
    template_name = 'clients/form.html'
    return render(request=request, template_name=template_name, context=context)
