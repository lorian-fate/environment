from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


# Create your models here.
class UserManager(BaseUserManager):
    """
        Esta clase permite que podamos crear usuarios con campos a parte de los que ya trae por defecto
        el propio django
    """
    def create_user(self, email, username, password=None):
        """ 
            Esta función nos permite crear usuarios
        """
        if not email:
            raise ValueError('A user must to have an Email')
        email = self.normalize_email(email)
        user = self.model(email=email, username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_superuser(self, username, email, password):
        """
            Esta función nos permite crear super usuarios
        """
        superuser = self.create_user(email, username, password)
        superuser.is_superuser = True
        superuser.is_staff = True
        superuser.save(using=self._db)
        return superuser

class Formation(models.Model):
    """
        Esta clase es un modelo para crear formaciones
    """
    formation_name = models.CharField(max_length=50)
    formation_created = models.DateTimeField(auto_now_add=True)
    formation_updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        """
            Esta clase permite que los datos se muestren de una forma específica
        """
        verbose_name = 'formation'
        verbose_name_plural = 'FORMATIONS'

    def __str__(self):
        return self.formation_name

class UserOver(AbstractUser):
    """
        Esta clase es un modelo para crear usuários
    """
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(verbose_name='E-mail', unique=True)
    username = models.CharField(max_length=50, unique=True)
    formation = models.ForeignKey(Formation, on_delete=models.CASCADE, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    user_created = models.DateTimeField(auto_now_add=True)
    user_updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        """
            Esta clase permite que los datos se muestren de una forma específica
        """
        verbose_name = 'user profiles'

    def __str__(self):
        return self.username
    
    objects = UserManager()