# Generated by Django 4.2.1 on 2023-05-31 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='prof_pic',
            field=models.ImageField(default='default.jpg', upload_to='profile_pics'),
        ),
    ]
