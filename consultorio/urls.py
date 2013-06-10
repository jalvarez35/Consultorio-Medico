from django.conf.urls import patterns, include, url
from historiaclinica.views import PacienteList, PacienteCreate, PacienteUpdate, PacienteDelete
from historiaclinica.views import HistoriaClinicaList, HistoriaClinicaCreate, HistoriaClinicaUpdate, HistoriaClinicaDelete
from django.contrib.auth.decorators import login_required as auth

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', PacienteList.as_view(), name='paciente_list'),
    url(r'^paciente/add/$', PacienteCreate.as_view(), name='paciente_add'),
    url(r'paciente/(?P<pk>\d+)/$', PacienteUpdate.as_view(), name='paciente_update'),
    url(r'paciente/(?P<pk>\d+)/delete/$', PacienteDelete.as_view(), name='paciente_delete'),
    
    url(r'^historiaclinica/list$', HistoriaClinicaList.as_view(), name='historiaclinica_list'),
    url(r'^historicaclinica/add/$', HistoriaClinicaCreate.as_view(), name='historiaclinica_add'),
    url(r'historiaclinica/(?P<pk>\d+)/$', HistoriaClinicaUpdate.as_view(), name='historiaclinica_update'),
    url(r'historiaclinica/(?P<pk>\d+)/delete/$', HistoriaClinicaDelete.as_view(), name='historiaclinica_delete'),

    url(r"^login/$", "django.contrib.auth.views.login",
       {"template_name": "login.html"}, name="login"),
    url(r"^logout/$", "django.contrib.auth.views.logout_then_login",
        name="logout"),
    url(r"^accounts/", include("registration.backends.simple.urls")),
)
