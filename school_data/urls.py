from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from college.views import CreateCollegeView
from school.views import CreateSchoolView, excelFile
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', CreateSchoolView.as_view(), name='home'),
    url(r'^college/$', CreateCollegeView.as_view(), name='college'),
    url(r'^excel/$', excelFile),
    # url(r'^school_data/', include('school_data.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

