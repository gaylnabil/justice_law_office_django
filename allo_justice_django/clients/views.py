from accounts.models import Types
from django.conf import settings
from django.db.models.query import QuerySet
from django.forms.models import inlineformset_factory, modelformset_factory
import pandas as pd
from clients.models import Client
from clients.forms import ClientAuthenticationForm, ClientCreationForm, ClientUpdateForm
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.utils.translation import gettext as _
from django.core.mail import EmailMultiAlternatives
from django.template import loader
from accounts.utils import WEEK_DAYS, account_activation_token
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text


# Create your views here.


def client_login(request):
    user = request.user
    if user and user.is_authenticated:
        return HttpResponseRedirect(reverse('home'))

    form = ClientAuthenticationForm(initial={'type': Types.ATTORNEY})

    if request.method == 'POST':
        # print('3 - client_login ==> POST')
        form = ClientAuthenticationForm(
            request=request, data=request.POST, initial={'type': Types.ATTORNEY})
        print('3 - client_login ==> ', form.is_valid())
        if form.is_valid():

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            # if remember_me:
            #         request.session['username'] = username
            #         request.session['password'] = password
            user = authenticate(
                request, username=username, password=password)

            if user is not None:

                login(request, user)
                # have to change this to list of projects of every Employee
                redirect_to = request.GET.get('next', 'home')
                return redirect(redirect_to)

            else:
                messages.error(
                    request, "le Nom d'utilisateur et le mot de passe est incorrecte !!!")

                return redirect('client_login')
        else:
            messages.error(
                request, "le Nom d'utilisateur et le mot de passe est incorrecte !!!")
            if 'next' in request.GET:
                redirect_to = request.GET.get('next', '')
                return redirect(redirect_to)

            return redirect('client_login')

    context = {
        'title': _('Client Login'),
        'inner_title': _('Client Login'),
        'breadcrumb': _('Client Login'),
        'form': form,
        'active_page': 'login',
    }
    return render(request, 'clients/login.html', context)


# def client_logout(request):
#     logout(request)
#     return redirect('home')


def client_register(request):

    user = request.user
    if user and user.is_authenticated:
        return HttpResponseRedirect(reverse('home'))

    form = ClientCreationForm(
        request.POST or None, initial={'is_active': False})

    if request.method == 'POST':

        if form.is_valid():
            user = form.save(commit=True)
            # user = form.save()
            # user.is_active = False
            recipients = [form.cleaned_data.get('email'), ]
            subject = _('Confirmez votre compte')
            scheme = request.scheme
            domain = get_current_site(request).domain
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            token = account_activation_token.make_token(user)
            # return HttpResponse([scheme, domain])
            activate = reverse('client_activate', kwargs={
                               'uidb64': uid, 'token': token})
            context = {
                'user': user,
                'scheme': scheme,
                'domain': domain,
                'activate': activate,
            }

            html_body = loader.render_to_string(
                'clients/activate.html', context=context)

            # email = EmailMultiAlternatives(
            #     subject=subject, from_email='gaylnabily@zohomail.com', to=recipients)
            # email.attach_alternative(html_body, "text/html")
            # email.send(fail_silently=False)

            email = EmailMultiAlternatives(
                subject=subject, from_email=settings.EMAIL_HOST_USER, to=recipients)
            email.attach_alternative(html_body, "text/html")
            email.send(fail_silently=False)

            # request.GET.get('verification', 'home')  # have to change this to list of projects of every Employee
            redirect_to = reverse('client_verification', kwargs={
                                  'email': user.email})
            return HttpResponseRedirect(redirect_to)

    value = _('Inscription de client')
    context = {
        'title': value,
        'inner_title': value,
        'breadcrumb': value,
        'form': form,
        'active_page': 'register',
    }
    return render(request, 'clients/register.html', context)


def client_verification(request, email):
    context = {
        'title': _('Vérification'),
        'inner_title': _('Vérification'),
        'breadcrumb': _('Vérification'),
        'email': email,
        'active_page': 'verification',
    }
    return render(request, 'clients/verification.html', context)


def client_activate(request, uidb64, token):
    uid = force_text(urlsafe_base64_decode(uidb64))
    user = Client.objects.filter(pk=uid).first()

    if user is not None and account_activation_token.check_token(user, token):
        # if valid set active true
        user.is_active = True
        # set signup_confirmation true
        user.save()
        login(request, user)
        return HttpResponseRedirect(reverse('home'))

    value = _('Activation Invalide')
    context = {
        'title': value,
        'inner_title': value,
        'breadcrumb': value,
        'active_page': 'invalidate',
    }
    return render(request, 'clients/invalidate_activate.html', context)


@login_required(login_url='client_login')
def client_profile(request):

    user = request.user
    if user and user.type == 'attorney':
        return HttpResponseRedirect(reverse('home'))

    client = request.user
    form = ClientUpdateForm(data=request.POST or None, instance=client)
    if request.method == 'POST':

        # valid = form.is_valid()
        # print(f'Nabil ===> {valid} ===> {request.user.address}')
        if form.is_valid():
            form.save()
            messages.success(request, _('Enregistrement est réussite !!'))
            # request.GET.get('verification', 'home')  # have to change this to list of projects of every Employee
            redirect_to = reverse('client_profile')
            return HttpResponseRedirect(redirect_to)

    # form = ClientUpdateForm(instance=client)
    context = {
        'title': _('Profile'),
        'inner_title': _('Mes informtation'),
        'breadcrumb': _('INformation d\'avocat'),
        'form': form,
        'active_page': 'profile',
    }
    return render(request, 'clients/profile.html', context)
