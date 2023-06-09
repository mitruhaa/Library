# Generated by Django 4.2.1 on 2023-05-18 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_alter_book_options_remove_book_isbn_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='bio',
            field=models.TextField(blank=True, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='summary',
            field=models.TextField(help_text='Enter a brief description of the book', max_length=2000),
        ),
    ]
