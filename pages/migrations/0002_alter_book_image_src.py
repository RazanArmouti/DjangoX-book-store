# Generated by Django 4.0 on 2021-12-08 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image_src',
            field=models.URLField(default='https://www.seekpng.com/png/detail/641-6410341_file-emojione-wikimedia-commons-png-transparent-book-book.png'),
        ),
    ]