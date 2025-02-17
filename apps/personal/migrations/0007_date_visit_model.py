# Generated by Django 4.1.6 on 2023-09-07 14:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('personal', '0006_remove_personal_model_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='Date_Visit_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_create', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_invite', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_finish', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='visitdate', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
