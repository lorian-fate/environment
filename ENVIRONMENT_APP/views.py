from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from .models import StudentFile
from .forms import StudentFileForms
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from ENVIRONMENT_MANAGE_APP.models import UserOver


# Create your views here.


@login_required
def userhome(request):
    """
        Esta función muestra los archivos correspondientes a un usuario previamente autenticado
    """
    student_file = {'student_F':StudentFile.objects.filter(exercice_author=request.user)}
    return render(request, 'ENVIRONMENT_APP/filehome.html', student_file)


@login_required
def details(request, id):
    """
        Esta función muestra mas detalladamente los distintos archivos que le corresponden a un 
        usuario habiendose autenticado previamente
    """
    file_obj = StudentFile.objects.filter(id=id)
    return render(request, 'ENVIRONMENT_APP/details.html', {'detail':file_obj})


@login_required
def createfile(request):
    """
        Esta función permite al usuario crear un nuevo archivo cuando este esta ubicando en su
        propio entorno
    """
    if request.method == 'POST':
        student_file = StudentFileForms(request.POST, request.FILES)
        if student_file.is_valid():
            student_file.save()
            return redirect('userhome')
    else:
        student_file = StudentFileForms()
    return render(request, 'ENVIRONMENT_APP/createfile.html', {'file':student_file}) 


@login_required
def updatefile(request, id):
    """
        Esta función permite al usuario editar un archivo cuando este esta ubicando en su
        propio entorno
    """
    obj = get_object_or_404(StudentFile, id = id)
    if request.method == 'POST':
        form_up = StudentFileForms(request.POST, request.FILES, instance=obj)
        if form_up.is_valid():
            form_up.save()
            return redirect('userhome')
    else:
        form_up = StudentFileForms(instance=obj)
    return render(request, 'ENVIRONMENT_APP/updatefile.html', {'file':form_up}) 


@login_required
def deletefile(request, id):
    """
        Esta función permite al usuario eliminar un archivo cuando este esta ubicando en su
        propio entorno
    """
    student_file_to_Delete = StudentFile.objects.filter(id = id)
    obj = get_object_or_404(StudentFile, id = id)
    if request.method == 'POST':
        obj.delete()
        return redirect('userhome')
    return render(request, 'ENVIRONMENT_APP/deletefile.html', {'file_to_delete':student_file_to_Delete})


