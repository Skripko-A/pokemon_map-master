# Generated by Django 5.0.6 on 2024-06-19 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0004_pokemonentity_pokemon'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='appeared_at',
            field=models.DateTimeField(null=True),
        ),
    ]
