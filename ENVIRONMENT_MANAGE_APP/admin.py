from django.contrib import admin
from .models import Formation, UserOver

# Register your models here.

class FormationAdmin(admin.ModelAdmin):
    """
        Esta clase permite visualizar las distintas formaciones en el entorno de administrador
    """
    formation_name = ('formation_name', 'formation_created')

class UserAdmin(admin.ModelAdmin):
    """
        Esta clase permite visualizar a los distintos usuarios en el entorno de administrador
    """
    user_ad = 'username'

admin.site.register(Formation, FormationAdmin)
admin.site.register(UserOver, UserAdmin)

