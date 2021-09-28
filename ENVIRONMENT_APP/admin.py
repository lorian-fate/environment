from django.contrib import admin
from .models import Category, StudentFile
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    """
        Esta clase nos permite visualizar las distintas categorias en el panel de administrador
    """
    category_file = ('category_name', 'category_created')

class StudentFileAdmin(admin.ModelAdmin):
    """
        Esta clase nos permite visualizar los distintos archivos en el panel de administrador
    """
    exercice_file = ('exercice_title','exercice_Statement')
    prepopulated_fields = {'slug': ('exercice_title',)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(StudentFile, StudentFileAdmin)
