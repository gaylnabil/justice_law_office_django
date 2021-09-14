from django.shortcuts import render

# Create your views here.


def index(request):

    context = {}
    template_name = 'index.html'
    return render(request=request, template_name=template_name, context=context)
