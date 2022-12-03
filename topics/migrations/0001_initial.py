# Generated by Django 4.1.3 on 2022-12-01 14:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Topics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('total_followers', models.IntegerField(default=0)),
                ('topic_creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_requests_created', to=settings.AUTH_USER_MODEL)),
                ('topic_followers', models.ManyToManyField(related_name='%(class)s_requests_followers', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]