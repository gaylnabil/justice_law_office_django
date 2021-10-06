from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.utils.translation import gettext_lazy as _
from affaires.models import AvocatCharge
from affaires.forms import AvocatChargeForm
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
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
AVOCAT_CHARGE_PER_PAGE = 3

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

    q = Q(search__icontains=search) & Q(search__icontains=city)
    if city == 'all':
       q = Q(search__icontains=search)

    total = AvocatCharge.objects.all().count()
    avocats_charges = AvocatCharge.objects.annotate(
        search=SearchVector('nom', 'prenom', 'ville')
    ).filter(q)

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
        'active_page': 'avocats_charges',
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
            # user = form.save()
            # redirect_to = reverse('justice_avocats_charges')

            redirect_to = reverse('justice_avocats_charges', kwargs={
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
        'active_page': 'avocats_charges',
        'breadcrumb': value,
        'form': form,
        'url_link': 'justice_avocats_charges_all'
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

    redirect_to = reverse('justice_avocats_charges_all')

    return HttpResponseRedirect(redirect_to)
