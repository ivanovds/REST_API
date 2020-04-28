# Generated by Django 3.0.5 on 2020-04-28 11:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0005_auto_20200426_2309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userloginactivitylog',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='login_activity', to=settings.AUTH_USER_MODEL),
        ),
    ]
