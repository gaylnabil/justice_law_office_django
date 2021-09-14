from django.shortcuts import render
from django.utils.translation import gettext_lazy as _
from clients.forms import ClientForm
# Create your views here.

def index(request):

    context = {
        'active_page': 'home',
    }
    template_name = 'justice/index.html'
    return render(request=request, template_name=template_name, context=context)
