# Generated by Django 4.1.3 on 2022-12-03 14:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0003_alter_topics_topic_creator'),
        ('room', '0004_merge_20221203_1950'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='room_topic',
        ),
        migrations.AlterField(
            model_name='room',
            name='topic',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='topics.topics'),
        ),
        migrations.DeleteModel(
            name='Topic',
        ),
    ]