from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.utils.translation import gettext_lazy as _
from clients.forms import ClientForm
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from clients.models import Client
from django.contrib.postgres.search import SearchVector, SearchQuery, TrigramSimilarity
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q, Count

# Create your views here.
CLIENTS_PER_PAGE = 4

def justice_clients(request):
    
    # user = request.user
    # if user and user.is_authenticated:
    #     return HttpResponseRedirect(reverse('home'))
    
    query = request.GET.get('query', '')
    page = request.GET.get('page', 1)
    total = Client.objects.all().count()
    clients = Client.objects.annotate(search=SearchVector('nom', 'prenom', 'ville', 'company')).filter(
        Q(search__icontains=query))
    print('clients : ', clients)
    
    paginator = Paginator(clients, CLIENTS_PER_PAGE)
    

    try:
        clients = paginator.page(page)
    except PageNotAnInteger:
        # page = CLIENTS_PER_PAGE
        clients = paginator.page(page)
    except EmptyPage:
        # page = paginator.num_pages
        clients = paginator.page(page)
    
    title = _('list des client')
    context = {
        'title': title + f' ({page})',
        'active_page': 'clients',
        'breadcrumb': title,
        'clients': clients,
        'page': clients.number,
        'query': query,
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
