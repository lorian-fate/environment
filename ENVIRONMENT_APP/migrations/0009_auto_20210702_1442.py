# Generated by Django 3.1.3 on 2021-07-02 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ENVIRONMENT_APP', '0008_auto_20210306_1206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentfile',
            name='slug',
            field=models.SlugField(default=models.CharField(max_length=50), max_length=250, unique_for_date='publish'),
        ),
    ]
