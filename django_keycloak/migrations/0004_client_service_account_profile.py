# Generated by Django 2.1.5 on 2019-02-19 13:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('django_keycloak', '0003_auto_20190204_1949'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='service_account_profile',
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.KEYCLOAK_OIDC_PROFILE_MODEL
            ),
        ),
    ]