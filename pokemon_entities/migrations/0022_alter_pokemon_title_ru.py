# Generated by Django 5.0.6 on 2024-06-22 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0021_alter_pokemonentity_health_points_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='title_ru',
            field=models.CharField(max_length=200, verbose_name='Название (рус)'),
        ),
    ]
