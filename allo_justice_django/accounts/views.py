from django.conf import settings
from django.db.models.query import QuerySet
from django.forms.models import inlineformset_factory, modelformset_factory
import pandas as pd
from django.core import serializers
from accounts.models import Attorney, Schedule, Types
from accounts.forms import AttorneyAuthenticationForm, AttorneyCreationForm, AttorneyUpdateForm, ScheduleAttorneyForm
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


# @login_required(login_url='user_login')
# def index(request):
#     context = {
#         'title': _('page d\'acceuil'),
#         'active_page': 'home',
#     }
#     return render(request, 'index.html', context)


def user_login(request):

    attorney = request.user
    if attorney and attorney.is_authenticated:
        return HttpResponseRedirect(reverse('home'))

    #obj = serializers.serialize('json', [data])
    form = AttorneyAuthenticationForm(initial={'type': Types.ATTORNEY})

    if request.method == 'POST':
        form = AttorneyAuthenticationForm(
            request=request, data=request.POST, initial={'type': Types.ATTORNEY})

        is_valid = form.is_valid()
        if is_valid:

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            # remember_me = form.cleaned_data.get('remember_me')
            # if remember_me:
            #         request.session['username'] = username
            #         request.session['password'] = password
            user = authenticate(request, username=username, password=password)

            if user is not None:

                # print(f'login : {remember_me}')
                # print(f'session :', request.session['username'])
                login(request, user)
                # have to change this to list of projects of every Employee
                redirect_to = request.GET.get('next', 'home')
                return redirect(redirect_to)

            # return redirect('projects_list')
        else:
            messages.info(request, 'Username or password is incorrect !!!')
            if 'next' in request.GET:
                redirect_to = request.GET.get('next', '')
                return redirect(redirect_to)

            return redirect('user_login')
    # else:

    #     form = AttorneyAuthenticationForm()
        # print(f'session after logout :', request.Cookie)
        # if request.session.has_key('username') and request.session.has_key('password'):
        #     username = request.session.get('username')
        #     password = request.session.get('password')
        #     form = AttorneyAuthenticationForm(initial={'username': username, 'password': password})

    value = _('Authentification d\'avocat')
    context = {
        'title': value,
        'inner_title': value,
        'breadcrumb': value,
        'form': form,
        'active_page': 'login',
    }
    return render(request, 'accounts/login.html', context)


def user_logout(request):
    logout(request)
    return redirect('home')


def user_register(request):
    attorney = request.user
    if attorney and attorney.is_authenticated:
        return HttpResponseRedirect(reverse('home'))

    form = AttorneyCreationForm(
        request.POST or None, initial={'is_active': False})

    if request.method == 'POST':

        if form.is_valid():
            attorney = form.save(commit=True)
            # user = form.save()
            # user.is_active = False
            recipients = [form.cleaned_data.get('email'), ]
            subject = _('Confirmez votre compte')
            scheme = request.scheme
            domain = get_current_site(request).domain
            uid = urlsafe_base64_encode(force_bytes(attorney.pk))
            token = account_activation_token.make_token(attorney)
            # return HttpResponse([scheme, domain])
            activate = reverse('user_activate', kwargs={
                               'uidb64': uid, 'token': token})
            context = {
                'user': attorney,
                'scheme': scheme,
                'domain': domain,
                'activate': activate,
            }

            html_body = loader.render_to_string(
                'accounts/activate.html', context=context)

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
                                  'email': attorney.email})
            return HttpResponseRedirect(redirect_to)

    value = _('Inscription d\'avocat')
    context = {
        'title': value,
        'inner_title': value,
        'breadcrumb': value,
        'form': form,
        'active_page': 'register',
    }
    return render(request, 'accounts/register.html', context)


def user_verification(request, email):
    context = {
        'title': _('Vérification'),
        'inner_title': _('Vérification'),
        'breadcrumb': _('Vérification'),
        'email': email,
        'active_page': 'verification',
    }
    return render(request, 'accounts/verification.html', context)


def user_activate(request, uidb64, token):
    uid = force_text(urlsafe_base64_decode(uidb64))
    user = Attorney.objects.filter(pk=uid).first()
    print('user Client: > ', user)
    if user is not None and account_activation_token.check_token(user, token):
        # if valid set active true
        user.is_active = True
        # set signup_confirmation true
        user.save()
        login(request, user)
        return redirect('home')

    context = {
        'title': _('Activation'),
        'inner_title': _('Activation'),
        'breadcrumb': _('Activation'),
        'active_page': 'invalidate',
    }
    return render(request, 'accounts/invalidate_activate.html', context)


@login_required(login_url='user_login')
def user_profile(request):

    user = request.user
    if user and user.type == 'clients':
        return HttpResponseRedirect(reverse('home'))

    form = AttorneyUpdateForm(
        data=request.POST or None, files=request.FILES or None, instance=user)
    if request.method == 'POST':

        # valid = form.is_valid()
        # print(f'Nabil ===> {valid} ===> {request.user.address}')
        if form.is_valid():
            form.save()
            messages.success(request, _('Enregistrement est réussite !!'))
            # request.GET.get('verification', 'home')  # have to change this to list of projects of every Employee
            redirect_to = reverse('user_profile')
            return HttpResponseRedirect(redirect_to)

    # form = AttorneyUpdateForm(instance=attorney)
    context = {
        'title': _('Profile'),
        'inner_title': _('Mes informtation'),
        'breadcrumb': _('INformation d\'avocat'),
        'form': form,
        'active_page': 'profile',
    }
    return render(request, 'accounts/profile.html', context)


@login_required(login_url='user_login')
def user_settings(request):

    user = request.user
    if user and user.type == 'clients':
        return HttpResponseRedirect(reverse('home'))

    ScheduleFormSet = inlineformset_factory(
        parent_model=Attorney,
        model=Schedule,
        form=ScheduleAttorneyForm,
        can_delete=False,
        extra=7,
        max_num=7
    )

    if request.method == 'POST':
        formset = ScheduleFormSet(request.POST, instance=user)
        print('formset.is_valid() : ', formset.is_valid())

        if formset.is_valid():
            formset.save(commit=True)

            messages.success(request, _('Enregistrement est réussite !!'))

            redirect_to = reverse('user_settings')
            return HttpResponseRedirect(redirect_to)

    # formset = ScheduleFormSet(initial=initial)
    initial = []
    count = Schedule.objects.filter(attorney=user).count()
    print('count :', count)
    print('initial :', initial)
    if count == 0:
        (Schedule(day_name=init['day_name'], time_from=init['day_name'],
                  time_to=init['day_name'], attorney=init['attorney']).save() for init in initial)

        for day in WEEK_DAYS:
            schedule = Schedule(day_name=day[0], time_from='08:00',
                                time_to='16:00', attorney=user)
            schedule.save()
            print('DAY : ', day)
            initial.append({'day_name': day, 'time_from': '08:00',
                            'time_to': '16:00', 'attorney': user})

    formset = ScheduleFormSet(initial=initial, instance=user)

    context = {
        'title': _('Paramétres'),
        'inner_title': _('Paramétres'),
        'breadcrumb': _('Paramétres d\'avocat'),
        'formset': formset,
        'active_page': 'profile',
    }

    return render(request, 'accounts/settings.html', context)
