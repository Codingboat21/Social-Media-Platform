# Generated by Django 4.2.3 on 2023-07-26 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_postliker_delete_post_liker'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profileimg',
            field=models.ImageField(default='Default_pfp.svg.png', upload_to='profile_images'),
        ),
    ]
