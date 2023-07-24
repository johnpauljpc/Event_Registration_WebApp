# Generated by Django 4.2.1 on 2023-07-23 11:22

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_user_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=django_resized.forms.ResizedImageField(crop=None, default='avatars/profile.jpeg', force_format=None, keep_meta=True, quality=-1, scale=None, size=[300, 300], upload_to=''),
        ),
    ]