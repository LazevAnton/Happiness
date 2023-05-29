# Generated by Django 4.2.1 on 2023-05-29 09:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('HappinessAPP', '0002_alter_members_options_alter_teams_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='HappinessLevel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.IntegerField(choices=[(1, 'Joy'), (2, 'Excitement'), (3, 'Gratitude'), (4, 'Pride'), (5, 'Optimism'), (6, 'Contentment'), (7, 'Love')])),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HappinessAPP.members')),
            ],
            options={
                'verbose_name_plural': 'HappinessLevel',
            },
        ),
    ]
