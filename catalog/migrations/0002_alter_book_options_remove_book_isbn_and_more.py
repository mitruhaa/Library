# Generated by Django 4.2.1 on 2023-05-14 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['title', 'status']},
        ),
        migrations.RemoveField(
            model_name='book',
            name='ISBN',
        ),
        migrations.RemoveField(
            model_name='book',
            name='pub_date',
        ),
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.ManyToManyField(help_text='Select a genre for this book', to='catalog.genre'),
        ),
    ]