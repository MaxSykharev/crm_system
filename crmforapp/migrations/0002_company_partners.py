# Generated by Django 4.0.3 on 2022-03-24 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crmforapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='partners',
            field=models.ManyToManyField(blank=True, to='crmforapp.company'),
        ),
    ]