"""justice_law_office URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns
from django.views.i18n import JavaScriptCatalog
# from django.contrib.messages.api import error
from django.urls import path, include
from django.conf.urls.static import static
# from django.conf.urls import handler404, handler500
# from project import errors
from django.views.static import serve
from django.contrib.auth import views as auth_views

urlpatterns = i18n_patterns(
    path('jsi18n/', JavaScriptCatalog.as_view(), name='javascript-catalog'),
    path('', include('clients.urls')),
    path('admin/', admin.site.urls),
    #path('accounts/avocats/', include('accounts.urls')),
    #path('accounts/clients/', include('clients.urls')),
    #path('accounts/', include('allauth.urls')),
    prefix_default_language=False
    # path('accounts/login/', auth_views.LoginView.as_view(template_name='views/login.html')),
    # path('error_404/', errors.error_404, name='error_404'),
    # path('error_500/', errors.error_500, name='error_500'),
)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
