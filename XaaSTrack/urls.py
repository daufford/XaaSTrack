from django.conf.urls import include, url
from django.contrib import admin, auth

from django.db.models.fields import CharField

urlpatterns = [
    # Examples:
    # url(r'^$', 'XaaSTrack.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^planman/', include('planman.urls')),
    url(r'^',include('django.contrib.auth.urls')),
    url(r'^accounts/login/$',auth.views.login),
]
