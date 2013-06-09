from django.conf.urls import patterns, include, url
from historiaclinica.views import PacienteList, PacienteCreate, PacienteUpdate, PacienteDelete
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', PacienteList.as_view(), name='paciente_list'),
    url(r'^paciente/add/$', PacienteCreate.as_view(), name='paciente_add'),
    url(r'paciente/(?P<pk>\d+)/$', PacienteUpdate.as_view(), name='paciente_update'),
    url(r'paciente/(?P<pk>\d+)/delete/$', PacienteDelete.as_view(), name='paciente_delete'),

)
