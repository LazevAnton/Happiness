# Generated by Django 4.2.1 on 2023-05-28 20:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HappinessAPP', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='members',
            options={'verbose_name_plural': 'Members'},
        ),
        migrations.AlterModelOptions(
            name='teams',
            options={'verbose_name_plural': 'Teams'},
        ),
    ]
