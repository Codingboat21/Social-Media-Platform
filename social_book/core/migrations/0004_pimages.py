# Generated by Django 4.2.3 on 2023-07-15 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_rename_psot_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='PImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='P_Images')),
            ],
        ),
    ]
