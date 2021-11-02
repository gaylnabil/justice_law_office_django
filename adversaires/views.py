from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.utils.translation import gettext_lazy as _
from adversaires.forms import AdversaireForm, AvocatAdversaireForm
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from adversaires.models import Adversaire, AvocatAdversaire
from django.contrib.postgres.search import SearchRank, SearchVector, SearchQuery, TrigramSimilarity
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


def justice_adversaires(request):


    # user = request.user
    # if user and user.is_authenticated:
    #     return HttpResponseRedirect(reverse('home'))
    try:
        query = request.GET.get('query', default='all-list')
        city = request.GET.get('city', default='all')
        page = request.GET.get('page', 1)
    
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
        
        vector = SearchVector('nom', 'prenom')
        multi_search = None
        if search != '':
            multi_search = SearchQuery(search)
        
            for word in search.split(' '):
                if multi_search is type(None):
                    multi_search = SearchQuery(word)
                else:
                    multi_search |= SearchQuery(word)
    
        if multi_search is None:
            if city != 'all':
                multi_search = SearchQuery(city)
                vector += SearchVector('ville')
        else:
            if city != 'all':
                multi_search &= SearchQuery(city)
                vector += SearchVector('ville')
    
        if multi_search is None and city == 'all':
           adversaires = Adversaire.objects.all()
        else:
            adversaires = Adversaire.objects.annotate(search=vector,
                                                      rank=SearchRank(
                                                          vector,
                                                          multi_search
                                                      )).filter(search=multi_search).order_by("-rank")
    
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
            'active_page': 3,
            'breadcrumb': title,
            'adversaires': adversaires,
            'page': adversaires.number,
            'url_pagination': 'justice_adversaires',
            'query': search,
            'cities': VILLES,
            'city':  city,
            'url_link': 'justice_adversaires'
        }
        template_name = 'adversaires/index.html'
    
    
        logger.info("Page list of 'Adversaires'.")
        return render(request=request, template_name=template_name, context=context)
    except:
      # logger.error(f"Error Adversaires Page; %s", traceback.format_exc())
      logger.error(f"Error Adversaires Page !!!", exc_info=True)


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

            redirect_to = reverse('justice_adversaires')

            value = _("L'adversaire")

            success = _('a été enregister avec succés ...')

            messages.info(request, f'{value} {adversaire} {success}')
            msg_log = f"'{adversaire}' {msg_log}"
            logger.info(msg_log)

            return HttpResponseRedirect(redirect_to)

    context = {
        'title': value,
        'active_page': 3,
        'breadcrumb': value,
        'form': form,
        'url_link': 'justice_adversaires'
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

    redirect_to = reverse('justice_adversaires')

    return HttpResponseRedirect(redirect_to)
    
    
# Attorney Opponents Views *************************************
def justice_avocats_adversaires(request):

    # user = request.user
    # if user and user.is_authenticated:
    #     return HttpResponseRedirect(reverse('home'))

    try:
        query = request.GET.get('query', default='all-list')
        city = request.GET.get('city', default='all')
        page = request.GET.get('page', 1)
    
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
              
        vector = SearchVector('nom', 'prenom')
        multi_search = None
        if search != '':
            multi_search = SearchQuery(search)
    
            for word in search.split(' '):
                if multi_search is type(None):
                    multi_search = SearchQuery(word)
                else:
                    multi_search |= SearchQuery(word)
    
        if multi_search is None:
            if city != 'all':
                multi_search = SearchQuery(city)
                vector += SearchVector('ville')
        else:
            if city != 'all':
                multi_search &= SearchQuery(city)
                vector += SearchVector('ville')
    
        if multi_search is None and city == 'all':
           avocats_advs = AvocatAdversaire.objects.all()
        else:
            avocats_advs = AvocatAdversaire.objects.annotate(search=vector,
                                                      rank=SearchRank(
                                                          vector,
                                                          multi_search
                                                      )).filter(search=multi_search).order_by("-rank")
    
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
            'active_page': 4,
            'breadcrumb': title,
            'avocats_advs': avocats_advs,
            'page': avocats_advs.number,
            'url_pagination': 'justice_avocats_adversaires',
            'query': search,
            'cities': VILLES,
            'city':  city,
            'url_link': 'justice_avocats_adversaires'
        }
        template_name = 'avocats_adversaires/index.html'
        
        logger.info("Page list of Avocats adversaires.")
    
        return render(request=request, template_name=template_name, context=context)
    except:
      # logger.error(f"Error Adversaires Page; %s", traceback.format_exc())
      logger.error(f"Error Avocats adversaires Page !!!", exc_info=True)


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

            redirect_to = reverse('justice_avocats_adversaires')

            value = _("L'avocat adversaire")

            success = _('a été enregister avec succés ...')

            messages.info(request, f'{value} {avocat_adv} {success}')
            
            msg_log = f"'{avocat_adv}' {msg_log}"
            logger.info(msg_log)

            return HttpResponseRedirect(redirect_to)

    context = {
        'title': value,
        'active_page': 4,
        'breadcrumb': value,
        'form': form,
        'url_link': 'justice_avocats_adversaires'
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
    
    redirect_to = reverse('justice_avocats_adversaires')

    return HttpResponseRedirect(redirect_to)
