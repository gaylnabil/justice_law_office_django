from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.utils.translation import gettext_lazy as _
from adversaires.forms import AdversaireForm, AvocatAdversaireForm
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from adversaires.models import Adversaire, AvocatAdversaire
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
ADVERSAIRE_PER_PAGE = 3
AVOCAT_ADVERSARIES_PER_PAGE = 3


def justice_adversaires_all(request):

    try:
        query = 'all-list'
        city = 'all'
        if request.method == 'POST':
            query = request.POST.get('query', default='all-list')
            city = request.POST.get('city', default='all')
            print(" => request.method => City :", city)

        query = 'all-list' if query == '' else query

        redirect_to = reverse('justice_adversaires', kwargs={
            'page': 1,
            'city': city,
            'query': slugify(query)
        }
        )
    except:
      # logger.error(f"Error Adversaires Page; %s", traceback.format_exc())
      logger.error(f"Error Adversaires Page !!!", exc_info=True)

    return HttpResponseRedirect(redirect_to)


def justice_adversaires(request, page=1, city='all', query='all-list'):

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

    # print('justice_adversaires => ', query, "Results : ", search, " => City :", city)

    q = Q(search__icontains=search) & Q(search__icontains=city)
    if city == 'all':
       q = Q(search__icontains=search)

    total = Adversaire.objects.all().count()
    adversaires = Adversaire.objects.annotate(
        search=SearchVector('nom', 'prenom', 'company', 'ville')
    ).filter(q)

    # print('search : ', search)
    search = 'all-list' if search == '' else search

    paginator = Paginator(adversaires, ADVERSAIRE_PER_PAGE)

    try:
        adversaires = paginator.page(page)
    except PageNotAnInteger:
        adversaires = paginator.page(page)
    except EmptyPage:
        adversaires = paginator.page(page)

    title = _('list des adversaires')
    context = {
        'title': title + f' ({page})',
        'active_page': 'adversaires',
        'breadcrumb': title,
        'adversaires': adversaires,
        'page': adversaires.number,
        'query': search,
        'cities': VILLES,
        'city':  city,
        'url_link': 'justice_adversaires_all'
    }
    template_name = 'adversaires/index.html'


    logger.info("Page list of 'Adversaires'.")
    return render(request=request, template_name=template_name, context=context)


def adversaire_form(request, id=0):
    value = ""
    form = None
    if request.method == 'GET':
        if id == 0:
            value = _("L'ajout d'adversaire")
            # form = AdversaireForm(initial={'type_adversaire': 1})
            form = AdversaireForm()
            msg_log = "Page Creating of 'Adversaire'"
        else:
            value = _("Modification d'Adversaire")
            adversaire = Adversaire.objects.filter(pk=id).first()
            form = AdversaireForm(instance=adversaire)
            msg_log = "Page Creating of 'Adversaire'"
            
    # print('request.method: ', request.method, " => id : ", id)

    if request.method == 'POST':
        if id == 0:
            form = AdversaireForm(request.POST)
            msg_log = "Adversaire has been Created."
        else:
            adversaire = Adversaire.objects.filter(pk=id).first()
            form = AdversaireForm(request.POST, instance=adversaire)
            msg_log = "Adversaire has been Updated."

        # print('form.is_valid(): ', form.is_valid())
        # print('request.get_full_path(): ',  request.get_full_path())

        if form.is_valid():
            adversaire = form.save(commit=True)
            # user = form.save()
            # redirect_to = reverse('justice_adversaires')

            redirect_to = reverse('justice_adversaires', kwargs={
                'page': 1,
                'city': 'all',
                'query': slugify(adversaire.nom)}
            )

            value = _("L'adversaire")

            success = _('a été enregister avec succés ...')

            messages.info(request, f'{value} {adversaire} {success}')
            msg_log = f"'{adversaire}' {msg_log}"
            logger.info(msg_log)

            return HttpResponseRedirect(redirect_to)

    context = {
        'title': value,
        'active_page': 'adversaires',
        'breadcrumb': value,
        'form': form,
        'url_link': 'justice_adversaires_all'
    }
    template_name = 'adversaires/form.html'
    
    logger.info(msg_log)
    
    return render(request=request, template_name=template_name, context=context)


def adversaire_delete(request, id=0):
    adversaire = Adversaire.objects.filter(pk=id).first()
    value = _("L'adversaire")
    success = _('a été supprimer avec succés ...')
    
    messages.info(request, f'{value} {adversaire} {success}')
    
    msg_log = f"Adversaire '{adversaire}' has been deleted successfully."
    logger.info(msg_log)

    adversaire.delete()

    redirect_to = reverse('justice_adversaires_all')

    return HttpResponseRedirect(redirect_to)
    
    
# Attorney Opponents Views *************************************
def justice_avocats_adversaires_all(request):

    try:
        query = 'all-list'
        city = 'all'
        if request.method == 'POST':
            
            query = request.POST.get('query', default='all-list')
            city = request.POST.get('city', default='all')
        
        query = 'all-list' if query == '' else query

        redirect_to = reverse('justice_avocats_adversaires', kwargs={
            'page': 1,
            'city': city,
            'query': slugify(query)
        }
        )

    except:
      # logger.error(f"Error Adversaires Page; %s", traceback.format_exc())
      logger.error(f"Error Avocats adversaires Page !!!", exc_info=True)

    return HttpResponseRedirect(redirect_to)


def justice_avocats_adversaires(request, page=1, city='all', query='all-list'):

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

    print('justice_avocats_adversaires => ', query,
          "Results : ", search, " => City :", city)

    q = Q(search__icontains=search) & Q(search__icontains=city)
    if city == 'all':
       q = Q(search__icontains=search)

    total = AvocatAdversaire.objects.all().count()
    avocats_advs = AvocatAdversaire.objects.annotate(
        search=SearchVector('nom', 'prenom', 'cabinet', 'ville')
    ).filter(q)

    print('search : ', search)
    search = 'all-list' if search == '' else search

    paginator = Paginator(avocats_advs, AVOCAT_ADVERSARIES_PER_PAGE)

    try:
        avocats_advs = paginator.page(page)
    except PageNotAnInteger:
        avocats_advs = paginator.page(page)
    except EmptyPage:
        avocats_advs = paginator.page(page)

    title = _('list des avocats adversaires')
    context = {
        'title': title + f' ({page})',
        'active_page': 'avocats_adversaires',
        'breadcrumb': title,
        'avocats_advs': avocats_advs,
        'page': avocats_advs.number,
        'query': search,
        'cities': VILLES,
        'city':  city,
        'url_link': 'justice_avocats_adversaires_all'
    }
    template_name = 'avocats_adversaires/index.html'
    
    logger.info("Page list of Avocats adversaires.")

    return render(request=request, template_name=template_name, context=context)


def avocat_adversaire_form(request, id=0):
    value = ""
    form = None
    if request.method == 'GET':

        if id == 0:
            value = _("L'ajout d'avocat adversaire")
            msg_log = "Page Creating of 'Avocat Adversaire'"
            # form = AdversaireForm(initial={'type_adversaire': 1})
           
            form = AvocatAdversaireForm()
        else:
            value = _("Modification d'avocat adversaire")
            avocat_adv = AvocatAdversaire.objects.filter(pk=id).first()
            form = AvocatAdversaireForm(instance=avocat_adv)
            
            msg_log = "Page Editing of 'Avocat Adversaire'"
            
            
    print('request.method: ', request.method, " => id : ", id)

    if request.method == 'POST':
        if id == 0:
            form = AvocatAdversaireForm(request.POST)
            msg_log = "Avocat Adversaire has been Created."
        else:
            avocat_adv = AvocatAdversaire.objects.filter(pk=id).first()
            form = AvocatAdversaireForm(request.POST, instance=avocat_adv)
            msg_log = "Avocat Adversaire has been Updated."

        print('form.is_valid(): ', form.is_valid())
        print('request.get_full_path(): ',  request.get_full_path())

        if form.is_valid():
            avocat_adv = form.save(commit=True)
            # user = form.save()
            # redirect_to = reverse('justice_avocat_adversaires')

            redirect_to = reverse('justice_avocats_adversaires', kwargs={
                'page': 1,
                'city': 'all',
                'query': slugify(avocat_adv.nom)}
            )

            value = _("L'avocat adversaire")

            success = _('a été enregister avec succés ...')

            messages.info(request, f'{value} {avocat_adv} {success}')
            
            msg_log = f"'{avocat_adv}' {msg_log}"
            logger.info(msg_log)

            return HttpResponseRedirect(redirect_to)

    context = {
        'title': value,
        'active_page': 'avocats_adversaires',
        'breadcrumb': value,
        'form': form,
        'url_link': 'justice_avocats_adversaires_all'
    }
    template_name = 'avocats_adversaires/form.html'
    
    logger.info(msg_log)
    
    return render(request=request, template_name=template_name, context=context)


def avocat_adversaire_delete(request, id=0):
    avocat_adv = AvocatAdversaire.objects.filter(pk=id).first()
    value = _("L'avocat adversaire")
    success = _('a été supprimer avec succés ...')

    messages.info(request, f'{value} {avocat_adv} {success}')

    msg_log = f"Avocat Adversaire '{avocat_adv}' has been deleted successfully."
    logger.info(msg_log)

    avocat_adv.delete()
    
    redirect_to = reverse('justice_avocats_adversaires_all')

    return HttpResponseRedirect(redirect_to)
