# Generated by Django 3.1.3 on 2021-03-04 10:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ENVIRONMENT_MANAGE_APP', '0004_auto_20210304_1121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userover',
            name='formation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ENVIRONMENT_MANAGE_APP.formation'),
        ),
    ]
