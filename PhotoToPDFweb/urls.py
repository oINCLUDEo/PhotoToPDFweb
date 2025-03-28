"""
URL configuration for PhotoToPDFweb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf.urls.static import static
from django.template.defaulttags import url
from django.urls import path, re_path, reverse_lazy
from django.views.generic.base import RedirectView
from main import views


urlpatterns = [
    re_path(r'^about/contact/', views.contact),
    re_path(r'^about', views.about),
    re_path('upload/', views.upload_files, name='upload_files'),
    re_path(r'^creating', views.creating, name='creating'),
    path('', views.index),
    re_path(r'^favicon\.ico$', RedirectView.as_view(url=reverse_lazy('staticfiles_url', kwargs={'path': 'icons/favicon.ico'}), permanent=True)),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

