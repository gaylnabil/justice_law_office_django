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
from django.template.defaultfilters import slugify
import string
import re
import logging
import traceback

from justice_law_office.constants import VILLES
logger = logging.getLogger(__name__)

# Create your views here.
CLIENTS_PER_PAGE = 3

def justice_clients_all(request):
    
    try:
        query = 'all-list'
        city = 'all'
        if request.method == 'POST':
            query = request.POST.get('query', default='all-list')
            city = request.POST.get('city', default='all')
            print(" => request.method => City :", city)
    
        query = 'all-list' if query == '' else query
       
        redirect_to = reverse('justice_clients', kwargs={
            'page': 1,
            'city': city,
            'query': slugify(query)
            }
        )
        
        logger.info("Getting Clients Page...")
    except:
      # logger.error(f"Error Clients Page; %s", traceback.format_exc())
      logger.error(f"Error Clients Page !!!", exc_info=True)
    
    return HttpResponseRedirect(redirect_to)
   
    
def justice_clients(request, page=1, city='all', query='all-list'):
    
    # user = request.user
    # if user and user.is_authenticated:
    #     return HttpResponseRedirect(reverse('home'))
    
    # query = request.GET.get('query', 'all')
    
    # page = request.GET.get('page', 1)
   
    query = query.strip()
    print(" 1- City :", city)
    search = query if query != 'all-list' else ''
    # city = get_key_dict(dict(VILLES), city)
    
    print(" 2- City :", city)
    # Create a regex pattern to match all special characters in string
    pattern = r'[' + string.punctuation + ']'
    # Remove special characters from the string
    search = re.sub(pattern, ' ', search)
    
    # print('justice_clients => ', query, "Results : ", search, " => City :", city)
    
    q = Q(search__icontains=search) & Q(search__icontains=city)
    if city == 'all':
       q  = Q(search__icontains=search)
    
    # total = Client.objects.all().count()
    clients = Client.objects.annotate(
        search=SearchVector('nom', 'prenom', 'company','ville') 
            ).filter(q)

    # print('search : ', search)
    search = 'all-list' if search == '' else search
    
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
        'active_page': 2,
        'breadcrumb': title,
        'clients': clients,
        'page': clients.number,
        'query': search,
        'cities': VILLES,
        'city':  city,
        'url_link': 'justice_clients_all'
    }
    template_name = 'clients/index.html'
    
    logger.info("Page list of 'Clients'.")
    
    return render(request=request, template_name=template_name, context=context)
    
    
def client_form(request, id=0):
    value = ""
    form = None
    if request.method == 'GET':
        if id == 0:
            value = _('L\'ajout de client')
            # form = ClientForm(initial={'type_client': 1})
            form = ClientForm()
            msg_log = "Page Creating of 'Client'"
        else:
            value = _('Modification de client')
            client = Client.objects.filter(pk=id).first()
            form = ClientForm(instance=client)
            msg_log = "Page Creating of 'Client'"
            
    # print('request.method: ', request.method, " => id : ", id)
    
    if request.method == 'POST':
        if id == 0:
            form = ClientForm(request.POST)
            msg_log = "Client has been Created."
        else:
            client = Client.objects.filter(pk=id).first()
            form = ClientForm(request.POST, instance=client)
            msg_log = "Client has been Updated."
            
        # print('form.is_valid(): ', form.is_valid())
        # print('request.get_full_path(): ',  request.get_full_path())
       
        if form.is_valid():
            client = form.save(commit=True)
            # user = form.save()
            # redirect_to = reverse('justice_clients')
            
            redirect_to = reverse('justice_clients', kwargs={
                'page': 1,
                'city': 'all',
                'query': slugify(client.nom)}
                )
                
            value = _('Le Client')
            
            success = _('a été enregister avec succés ...')
            
            messages.info(request, f'{value} {client} {success}')
            msg_log = f"'{client}' {msg_log}"
            logger.info(msg_log)
            
           
                
            return HttpResponseRedirect(redirect_to)
            
    
        
    context = {
        'title': value,
        'active_page': 2,
        'breadcrumb': value,
        'form': form,
        'url_link': 'justice_clients_all'
    }
    template_name = 'clients/form.html'
    
    logger.info(msg_log)
    
    return render(request=request, template_name=template_name, context=context)
    
    
def client_delete(request, id=0):
    client = Client.objects.filter(pk=id).first()
    value = _('Le Client')
    success = _('a été supprimer avec succés ...')
    
    messages.info(request, f'{value} {client} {success}')
    
    msg_log = f"Adversaire '{client}' has been deleted successfully."
    logger.info(msg_log)
    
    client.delete()
    
    redirect_to = reverse('justice_clients_all')
    
    return HttpResponseRedirect(redirect_to)
