# Generated by Django 3.1.3 on 2021-03-04 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=50)),
                ('category_created', models.DateTimeField(auto_now_add=True)),
                ('category_updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='StudentFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exercice_title', models.CharField(max_length=50)),
                ('exercice_Statement', models.TextField()),
                ('exercice_file', models.FileField(upload_to='files')),
                ('exercice_created', models.DateTimeField(auto_now_add=True)),
                ('exercice_updated', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
