from django.contrib import admin
from .models import Paciente, HistoriaClinica, UserProfile
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

class PacienteAdmin(admin.ModelAdmin):
    pass
admin.site.register(Paciente, PacienteAdmin)

class HistoriaClinicaAdmin(admin.ModelAdmin):
    pass
admin.site.register(HistoriaClinica, HistoriaClinicaAdmin)

class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False

class UserProfileAdmin(UserAdmin):
    inlines=(UserProfileInline, )

admin.site.unregister(get_user_model())
admin.site.register(get_user_model(), UserProfileAdmin)
