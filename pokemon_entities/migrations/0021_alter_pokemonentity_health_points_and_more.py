# Generated by Django 5.0.6 on 2024-06-21 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0020_alter_pokemonentity_pokemon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemonentity',
            name='health_points',
            field=models.IntegerField(blank=True, default=0, verbose_name='Очки здоровья'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='level',
            field=models.IntegerField(blank=True, default=0, verbose_name='Уровень'),
        ),
    ]