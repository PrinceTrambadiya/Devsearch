# Generated by Django 4.1.7 on 2024-02-13 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(blank=True, default='images/profiles/user-default.png', null=True, upload_to='profiles/'),
        ),
    ]