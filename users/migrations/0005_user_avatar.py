# Generated by Django 4.2.1 on 2023-05-30 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_user_hackthon_participant'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default='avatars/profile.jpeg', null=True, upload_to=''),
        ),
    ]
