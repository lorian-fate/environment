from django import forms
from .models import StudentFile

class StudentFileForms(forms.ModelForm):
    """
        Esta clase nos permite crear un formulario a partir del modelo StudentFile
    """
    class Meta:
        model = StudentFile
        fields = ['exercice_title',
                'exercice_Statement',
                'exercice_author',
                'exercice_category', 
                'exercice_file']


#'exercice_author', 
#exercice_author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
  