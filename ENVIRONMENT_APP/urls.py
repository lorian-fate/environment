from django.urls import path
from . import views

urlpatterns = [
    path('userhome/', views.userhome, name = 'userhome'),
    path('createfile/', views.createfile, name = 'create'),
    path('<id>/delete', views.deletefile, name = 'delete'),
    path('<id>/detail', views.details, name = 'detail'),
    path('<int:id>/', views.updatefile, name = 'update'),
    
    

]
