# Generated by Django 4.2.1 on 2023-05-31 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_remove_user_prof_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='prof_pic',
            field=models.ImageField(default='default.jpg', upload_to='profile_pics'),
        ),
    ]
