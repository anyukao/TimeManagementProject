# Generated by Django 4.1.6 on 2024-02-13 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0014_date_visit_model_pause_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='date_visit_model',
            name='summ_pause_time',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Общий перерыв'),
        ),
    ]
