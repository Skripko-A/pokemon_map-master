# Generated by Django 5.0.6 on 2024-06-20 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0011_remove_pokemon_title_pokemon_title_en_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='title_ru',
            field=models.CharField(default='pokemon_unnamed', max_length=200),
        ),
    ]
