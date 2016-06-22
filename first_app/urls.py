from django.conf.urls import include, url
from django.contrib import admin

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    # Examples:
    url(r'^$', 'joins.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^(?P<ref_id>.*)$', 'joins.views.share', name='share'),
    # url(r'^blog/', include('blog.urls')),


]
