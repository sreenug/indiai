from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from school.views import CreateSchoolView
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', CreateSchoolView.as_view(), name='home'),
    # url(r'^school_data/', include('school_data.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

