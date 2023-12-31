# Generated by Django 4.2.3 on 2023-07-11 23:06

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Psot',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('user', models.CharField(max_length=100)),
                ('caption', models.TextField()),
                ('image', models.ImageField(upload_to='post_image')),
                ('no_of_likes', models.IntegerField(default=0)),
                ('created_at', models.DateField(default=datetime.datetime.now)),
            ],
        ),
    ]
