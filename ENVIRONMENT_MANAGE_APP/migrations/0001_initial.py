# Generated by Django 3.1.3 on 2021-03-04 10:10

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Formation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('formation_name', models.CharField(max_length=50)),
                ('formation_created', models.DateTimeField(auto_now_add=True)),
                ('formation_updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'formation',
                'verbose_name_plural': 'FORMATIONS',
            },
        ),
        migrations.CreateModel(
            name='UserOver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='E-mail')),
                ('username', models.CharField(max_length=50, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=True)),
                ('is_superuser', models.BooleanField(default=False)),
                ('user_created', models.DateTimeField(auto_now_add=True)),
                ('user_updated', models.DateTimeField(auto_now_add=True)),
                ('formation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ENVIRONMENT_MANAGE_APP.formation')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user profiles',
            },
        ),
    ]
