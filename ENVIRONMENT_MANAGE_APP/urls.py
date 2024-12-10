

from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
#from django.conf.urls import url
from django.urls import re_path as url
from django.views.static import serve
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('tag/<slug:tag_slug>/', views.home, name='file_by_tag'),
    path('sign_up/', views.sign_up, name='sign'),

    path('search/', views.file_search, name='file_search'),
    #path('login/', views.log_in, name='log_in'),
    #path('login/', views.log_out, name='logout'),
    path('login/', auth_views.LoginView.as_view(), name='log_in'),
    #path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    
    path('', include('django.contrib.auth.urls')),

    path('administrator/', views.administrator, name='admin'),
    path('<int:year>/<int:month>/<int:day>/<slug:file_detail>/', views.file_detail, name='file_detail'),
    path('filter/', views.filter_ca, name='filter'),
    path('categories/<int:category_id>/', views.filtered, name='filtered'),
    url(r'^download/(?P<path>.*)$', serve, {'document_root':settings.MEDIA_ROOT}),

    
]
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


