from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.utils.translation import gettext_lazy as _
from clients.forms import ClientForm
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from clients.models import Client
# Create your views here.

def justice_clients(request):
    
    # user = request.user
    # if user and user.is_authenticated:
    #     return HttpResponseRedirect(reverse('home'))
    clients = Client.objects.all()
    value = _('list des client')
    context = {
        'title': value,
        'active_page': 'clients',
        'breadcrumb': value,
        'clients': clients,
    }
    template_name = 'clients/index.html'
         
    return render(request=request, template_name=template_name, context=context)
    
    
def client_form(request, id=0):
    value = ""
    form = None
    if request.method == 'GET':
        if id == 0:
            value = _('L\'ajout de client')
            # form = ClientForm(initial={'type_client': 1})
            form = ClientForm()
        else:
            value = _('Modification de client')
            client = Client.objects.filter(pk=id).first()
            form = ClientForm(instance=client)
    print('request.method: ', request.method, " => id : ", id)
    
    if request.method == 'POST':
        if id == 0:
            form = ClientForm(request.POST)
        else:
            client = Client.objects.filter(pk=id).first()
            form = ClientForm(request.POST, instance=client)
            
        print('form.is_valid(): ', form.is_valid())
        print('request.get_full_path(): ',  request.get_full_path())
       
        if form.is_valid():
            client = form.save(commit=True)
            # user = form.save()
            redirect_to = reverse('justice_clients')
            
            value = _('Le Client')
            
            success = _('a été enregister avec succés ...')
            
            messages.info(request, f'{value} {client} {success}')
            return HttpResponseRedirect(redirect_to)
            
    
        
    context = {
        'title': value,
        'active_page': 'clients',
        'breadcrumb': value,
        'form': form,
    }
    template_name = 'clients/form.html'
    return render(request=request, template_name=template_name, context=context)
    
    
def client_delete(request, id=0):
    client = Client.objects.filter(pk=id).first()
    value = _('Le Client')
    success = _('a été supprimer avec succés ...')
    
    messages.info(request, f'{value} {client} {success}')
    
    client.delete()
    
    redirect_to = reverse('justice_clients')
    
    return HttpResponseRedirect(redirect_to)
