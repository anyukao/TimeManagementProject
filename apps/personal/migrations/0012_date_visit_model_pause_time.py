# Generated by Django 4.1.6 on 2024-02-13 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0011_personal_model_date_deactivate'),
    ]

    operations = [
        migrations.AddField(
            model_name='date_visit_model',
            name='pause_time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
