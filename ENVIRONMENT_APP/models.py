from django.db import models
from ENVIRONMENT_MANAGE_APP.models import UserOver as user
from taggit.managers import TaggableManager
from django.utils import timezone
from django.urls import reverse
from django.template import defaultfilters
# Create your models here.



class Category(models.Model):
    """
        Esta clase es un modelo que nos permite clasificar los ejercicio en categorias
    
    """
    category_name = models.CharField(max_length=50)
    category_created = models.DateTimeField(auto_now_add=True)
    category_updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.category_name


class StudentFile(models.Model):
    """
        Esta clase es un modelo para la inserción de los datos correspondientes a un archivo
    """
    exercice_title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    exercice_Statement = models.TextField()
    exercice_file = models.FileField(upload_to='files')
    exercice_author = models.ForeignKey(user, on_delete=models.DO_NOTHING)
    exercice_category = models.ManyToManyField(Category)
    publish = models.DateTimeField(default=timezone.now)
    exercice_created = models.DateTimeField(auto_now_add=True)
    exercice_updated = models.DateTimeField(auto_now=True)
    tags = TaggableManager()



    class Meta:
        ordering = ('-publish',)
    
    def save(self, *args, **kwargs):
      self.slug = defaultfilters.slugify(self.exercice_title)
      super(StudentFile, self).save(*args, **kwargs)

    def __str__(self):
        return self.exercice_title
    
    def get_absolute_url(self):
        return reverse('file_detail',
                       args=[self.publish.year,
                             self.publish.month,
                             self.publish.day,
                             self.slug])

    

