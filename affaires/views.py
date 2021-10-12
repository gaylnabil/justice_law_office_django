from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.utils.translation import gettext_lazy as _
from affaires.models import AvocatCharge, Departement
from affaires.forms import AvocatChargeForm, DepartementForm
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.postgres.search import SearchVector, SearchQuery, TrigramSimilarity
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q, Count, query_utils
from django.template.defaultfilters import slugify
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
from urllib.parse import unquote

import string
import re
import logging
import traceback

from justice_law_office.constants import VILLES

logger = logging.getLogger(__name__)

# Create your views here.
AVOCAT_CHARGE_PER_PAGE = 3
DEPARTEMENT_PER_PAGE = 3

# Attorney Charge Views *************************************
def justice_avocats_charges_all(request):

    try:
        query = 'all-list'
        city = 'all'
        if request.method == 'POST':

            query = request.POST.get('query', default='all-list')
            city = request.POST.get('city', default='all')

        query = 'all-list' if query == '' else query

        redirect_to = reverse('justice_avocats_charges', kwargs={
            'page': 1,
            'city': city,
            'query': slugify(query)
        }
        )

    except:
      # logger.error(f"Error charges Page; %s", traceback.format_exc())
      logger.error(f"Error Avocats charges Page !!!", exc_info=True)

    return HttpResponseRedirect(redirect_to)


def justice_avocats_charges(request, page=1, city='all', query='all-list'):

    # user = request.user
    # if user and user.is_authenticated:
        #     return HttpResponseRedirect(reverse('home'))

    # query = request.GET.get('query', 'all')

    # page = request.GET.get('page', 1)

    query = query.strip()
    search = query if query != 'all-list' else ''
    print(" 2- City :", city)
    # Create a regex pattern to match all special characters in string
    pattern = r'[' + string.punctuation + ']'
    # Remove special characters from the string
    search = re.sub(pattern, ' ', search)

    print('justice_avocats_charges => ', query,
          "Results : ", search, " => City :", city)

    query = SearchQuery(search) & SearchQuery(city)
    if city == 'all':
        query = SearchQuery(search)
    vector = SearchVector('nom', 'prenom', 'ville')

    print("Query: ", query, " => search : ", search)

    print('vector: ', vector)

    # total = Client.objects.all().count()
    if city == 'all' and search == '':
        avocats_charges = AvocatCharge.objects.annotate(search=vector)
    else:
        avocats_charges = AvocatCharge.objects.annotate(search=vector).filter(search=query)
    
    print('search : ', search)
    search = 'all-list' if search == '' else search

    paginator = Paginator(avocats_charges, AVOCAT_CHARGE_PER_PAGE)

    try:
        avocats_charges = paginator.page(page)
    except PageNotAnInteger:
        avocats_charges = paginator.page(page)
    except EmptyPage:
        avocats_charges = paginator.page(page)

    title = _('list des avocats charges')
    context = {
        'title': title + f' ({page})',
        'active_page': 5,
        'breadcrumb': title,
        'avocats_charges': avocats_charges,
        'page': avocats_charges.number,
        'query': search,
        'cities': VILLES,
        'city':  city,
        'url_link': 'justice_avocats_charges_all'
    }
    template_name = 'affaires/avocats_charges/index.html'

    logger.info("Page list of Avocats charges.")

    return render(request=request, template_name=template_name, context=context)


def avocat_charge_form(request, id=0):
    value = ""
    form = None
    if request.method == 'GET':

        if id == 0:
            value = _("L'ajout d'avocat chargé")
            msg_log = "Page Creating of 'Avocat chargé'"

            form = AvocatChargeForm()
        else:
            value = _("Modification d'avocat chargé")
            avocat_charge = AvocatCharge.objects.filter(pk=id).first()
            form = AvocatChargeForm(instance=avocat_charge)

            msg_log = "Page Editing of 'Avocat chargé'"

    print('request.method: ', request.method, " => id : ", id)

    if request.method == 'POST':
        if id == 0:
            form = AvocatChargeForm(request.POST)
            msg_log = "Avocat chargé has been Created."
        else:
            avocat_charge = AvocatCharge.objects.filter(pk=id).first()
            form = AvocatChargeForm(request.POST, instance=avocat_charge)
            msg_log = "Avocat chargé has been Updated."

        print('form.is_valid(): ', form.is_valid())
        print('request.get_full_path(): ',  request.get_full_path())

        if form.is_valid():
            avocat_charge = form.save(commit=True)

            redirect_to = reverse('departements_views', kwargs={
                'page': 1,
                'city': 'all',
                'query': slugify(avocat_charge.nom)}
            )

            value = _("L'avocat chargé")

            success = _('a été enregister avec succés ...')

            messages.info(request, f'{value} {avocat_charge} {success}')

            msg_log = f"'{avocat_charge}' {msg_log}"
            logger.info(msg_log)

            return HttpResponseRedirect(redirect_to)

    context = {
        'title': value,
        'active_page': 5,
        'breadcrumb': value,
        'form': form,
        'url_link': 'departements_all'
    }
    template_name = 'affaires/avocats_charges/form.html'

    logger.info(msg_log)

    return render(request=request, template_name=template_name, context=context)


def avocat_charge_delete(request, id=0):
    avocat_charge = AvocatCharge.objects.filter(pk=id).first()
    value = _("L'avocat chargé")
    success = _('a été supprimer avec succés ...')

    messages.info(request, f'{value} {avocat_charge} {success}')

    msg_log = f"Avocat chargé '{avocat_charge}' has been deleted successfully."
    logger.info(msg_log)

    avocat_charge.delete()

    redirect_to = reverse('departements_all')

    return HttpResponseRedirect(redirect_to)
    
    
# Departments Views *************************************


# Attorney Charge Views *************************************
def departements_all(request):

    try:
        query = 'all-list'
        
        if request.method == 'POST':
            query = request.POST.get('query', default='all-list')
        
        query = 'all-list' if query == '' else query

        redirect_to = reverse('departements_views', kwargs={
            'page': 1,
            'query': query
        })

    except:
      # logger.error(f"Error charges Page; %s", traceback.format_exc())
      logger.error(f"Error Avocats charges Page !!!", exc_info=True)

    return HttpResponseRedirect(redirect_to)
    
    
def departements_views(request, page=1, query='all-list'):

    # user = request.user
    # if user and user.is_authenticated:
    #     return HttpResponseRedirect(reverse('home'))

    # query = request.GET.get('query', 'all')

    # page = request.GET.get('page', 1)

    query = query.strip()
    search = query if query != 'all-list' else ''
    # Create a regex pattern to match all special characters in string
    pattern = r'[' + string.punctuation + ']'
    # Remove special characters from the string
    search = re.sub(pattern, ' ', search)

    print('departements_views => ', query, "; Results : ", search)
    
    vector = SearchVector('nom_depart')
    
    multi_search = None
    for word in search.split(' '):
        if multi_search is None:
            multi_search = Q(search__contains=word)
        else:
            multi_search |= Q(search__contains=word)
    
    
    # query = SearchQuery(unquote(search))

    print("multi_search: ", multi_search,
          " => search.split(' ') : ", search.split(' '))

    print('vector: ', vector)

    departements = Departement.objects.annotate(search=vector).filter(multi_search)
    # total = Client.objects.all().count()
    if search == '':
        departements = Departement.objects.annotate(search=vector)

    print('search : ', search)
    search = 'all-list' if search == '' else search

    paginator = Paginator(departements, DEPARTEMENT_PER_PAGE)

    try:
        departements = paginator.page(page)
    except PageNotAnInteger:
        departements = paginator.page(page)
    except EmptyPage:
        departements = paginator.page(page)

    template_name = 'affaires/departements/index.html'
    
    
    # Departement form
    
    form = DepartementForm()

    title = _('list de Departements')
    context = {
        'title': title + f' ({page})',
        'active_page': 6,
        'breadcrumb': title,
        'departements': departements,
        'page': departements.number,
        'url_pagination': 'departements_views',
        'query': search,
        'url_link': 'departements_all',
        'form': form,
        'add_title': _("information de departement"),
        
    }
    
    logger.info("Page list of Departements.")

    return render(request=request, template_name=template_name, context=context)
    

def departement_data(request, id=0):
    
    departement = Departement.objects.filter(pk=id).first()
    if departement:
        return departement

    return None

def departement_form(request, id=0):
    value = ""
    form = None
    if request.method == 'GET':

        if id == 0:
            value = _("L'ajout de departement")
            msg_log = "Page Creating of 'Departement'"

            form = DepartementForm()
        else:
            value = _("Modification de Departement")
            departement = Departement.objects.filter(pk=id).first()
            data = Departement.objects.filter(pk=id).values().first()
            msg_log = f"Pop up Editing of 'Departement' {departement}"
            logger.info(msg_log)
            
            print('data: ', data)
            
            return JsonResponse({'departement': data}, safe=False)


    print('request.method: ', request.method, " => id : ", id)

    if request.method == 'POST':
        if id == 0:
            form = DepartementForm(request.POST)
            msg_log = "Departement has been Created."
        else:
            departement = Departement.objects.filter(pk=id).first()
            form = DepartementForm(request.POST, instance=departement)
            msg_log = "Departement has been Updated."

        print('form.is_valid(): ', form.is_valid())
        print('request.get_full_path(): ',  request.get_full_path())

        if form.is_valid():
            departement = form.save(commit=True)

            redirect_to = reverse('departements_views', kwargs={
                'page': 1,
                'query': slugify(departement.nom_depart)}
            )

            value = _("Le Departement")

            success = _('a été enregister avec succés ...')

            messages.info(request, f'{value} {departement} {success}')

            msg_log = f"'{departement}' {msg_log}"
            logger.info(msg_log)

            return HttpResponseRedirect(redirect_to)

    context = {
        'title': value,
        'active_page': 5,
        'breadcrumb': value,
        'form': form,
        'url_link': 'departements_all',
     
    }
    template_name = 'affaires/departements/form.html'

    logger.info(msg_log)

    return render(request=request, template_name=template_name, context=context)


def departement_delete(request, id=0):
    departement = Departement.objects.filter(pk=id).first()
    value = _("Le Departement")
    success = _('a été supprimer avec succés ...')

    messages.info(request, f'{value} {departement} {success}')

    msg_log = f"Departement '{departement}' has been deleted successfully."
    logger.info(msg_log)

    departement.delete()

    redirect_to = reverse('departements_all')

    return HttpResponseRedirect(redirect_to)
