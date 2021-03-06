"""hinga-weze-procurement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
# noinspection PyProtectedMember
from django.urls import path
from django.views.generic import TemplateView

from api.views import api_operator_views
from backend.views import operator_views

urlpatterns = [
    # url(r'', include('shrink.urls')),
    url(r'^tinymce/', include('tinymce.urls')),
    # url(r'^attachments/', include('attachments.urls', namespace='attachments')),
    path('admin/', admin.site.urls),
    path('backend/', include('backend.urls')),
    url(r'^$', operator_views.signin, name='signin'),
    url(r'^service-worker.js',
        (TemplateView.as_view(template_name="service-worker/service-worker.js",
                              content_type='application/javascript', )),
        name='service-worker.js'),

    # external api routes
    # operators
    url(r'^apis/operators/login/$', api_operator_views.operator_login, name='api_operators_login'),
    url(r'^apis/operators/$', api_operator_views.operators, name='api_operators'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if settings.DEBUG:
#     import debug_toolbar
#     urlpatterns = [
#                       url(r'^__debug__/', include(debug_toolbar.urls)),
#                   ] + urlpatterns
