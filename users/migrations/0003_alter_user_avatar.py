# Generated by Django 4.2.1 on 2023-07-23 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default='avatars/profile.jpeg', null=True, upload_to=''),
        ),
    ]