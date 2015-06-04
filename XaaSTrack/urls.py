from django.conf.urls import include, url
from django.contrib import admin, auth

from django.db.models.fields import CharField
from planman.views import register

urlpatterns = [
    # Examples:
    # url(r'^$', 'XaaSTrack.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^planman/', include('planman.urls')),
    url(r'^',include('planman.urls')),

    ##Use stock auth views:
    ###https://docs.djangoproject.com/en/1.8/topics/auth/default/#module-django.contrib.auth.views
    url(r'^',include('django.contrib.auth.urls')),
    url(r'^register/',register,name="register")
]

# Build-in stock auth urls
# ^login/$ [name='login']
# ^logout/$ [name='logout']
# ^password_change/$ [name='password_change']
# ^password_change/done/$ [name='password_change_done']
# ^password_reset/$ [name='password_reset']
# ^password_reset/done/$ [name='password_reset_done']
# ^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$ [name='password_reset_confirm']
# ^reset/done/$ [name='password_reset_complete']