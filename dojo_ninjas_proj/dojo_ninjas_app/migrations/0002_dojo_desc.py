# Generated by Django 3.2.7 on 2021-09-14 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dojo_ninjas_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dojo',
            name='desc',
            field=models.CharField(default='dojo antiguo', max_length=255),
        ),
    ]