from django.shortcuts import render, HttpResponseRedirect, redirect, get_object_or_404
from .forms import User_ProfilesForm, LoginForm, SearchForm
from ENVIRONMENT_APP.models import StudentFile, Category
from django.contrib.auth import login, authenticate
from django.http import HttpResponse, Http404, HttpResponseRedirect
import os
from taggit.models import Tag
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import  Count
from django.contrib.postgres.search import  SearchVector, SearchQuery, SearchRank

# Create your views here.

def home(request, tag_slug=None):
    """
        Esta función define la estructura principal con los archivos a mostra y la forma
    """
    obj = StudentFile.objects.all()
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        obj = obj.filter(tags__in=[tag])
    
    paginator = Paginator(obj, 2) # 2 post in each page
    page = request.GET.get('page')
    try:
        stud = paginator.page(page)
    except PageNotAnInteger:
        stud = paginator.page(1)
    except EmptyPage:
        stud = paginator.page(paginator.num_pages)
    return render(request, 'ENVIRONMENT_MANAGE_APP/mainhome.html', {'page':page, 'stud':stud, 'tag':tag})


def file_detail(request, year, month, day, file_detail):
    """
        Esta función mustra mas detalladamente los archivos
    """

    obj_file = get_object_or_404(StudentFile, slug=file_detail, publish__year=year, publish__month=month, publish__day=day)
    file_tags_id = obj_file.tags.values_list('id', flat=True)
    similar_file = StudentFile.objects.filter(tags__in=file_tags_id).exclude(id=obj_file.id)
    similar_file = similar_file.annotate(same_tags=Count('tags')).order_by('-same_tags', '-publish')[:4]
    return render(request, 'ENVIRONMENT_MANAGE_APP/file_home.html', {'obj_file':obj_file, 'similar_file':similar_file})



def download(request, path):
    """
        Esta función permite descargar los archivos disponibles
    """
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fl:
            response = HttpResponse(fl.read(), content_type = "application/exercice_file")
            response['Content-Disposition'] = 'inline;filename='+os.path.basename(file_path)
            return response
    raise Http404


def sign_up(request):
    """
        Esta función permite el registro de nuevos usuarios
    """
    if request.method == 'POST':
        user_form = User_ProfilesForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect('log_in')
    else:
        user_form = User_ProfilesForm()
    return render(request, 'ENVIRONMENT_MANAGE_APP/form.html', {'sign_up_form':user_form})


def administrator(request):
    """
        Esta función permite acceder al entorno de administrador
    """
    return HttpResponseRedirect('/admin/')


def log_in(request):
    """
        Esta función permite que los usuarios puedan autenticarse para acceder a sus entornos
    """
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated', 'successfully')
                else:
                    return HttpResponse('Disable account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'ENVIRONMENT_MANAGE_APP/login.html', {'form':form})


def file_search(request):
    """
        Esta función nos permite hacer una busqueda de archivos
    """
    form = SearchForm()
    query = None
    results = []
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            search_vector = SearchVector('exercice_title', weight='A') + SearchVector('exercice_Statement', weight='B')
            search_query = SearchQuery(query)
            results = StudentFile.objects.annotate(rank=SearchRank(search_vector, search_query)).filter(rank__gte=0.3).order_by('-rank')
    return render(request, 'ENVIRONMENT_MANAGE_APP/mainhome.html', {'form':form, 'query':query, 'results':results})


def filter_ca(request):
    """

    """
    return render(request, 'ENVIRONMENT_MANAGE_APP/filter.html', {'category':Category.objects.all()})


def filtered(request, category_id):
    """
        Esta función nos permite filtrar los archivos por categorias
    """
    category = Category.objects.get(id=category_id)
    student_file = {'student_File':StudentFile.objects.filter(exercice_category=category)}
    return render(request, 'ENVIRONMENT_MANAGE_APP/filtered.html', student_file)

