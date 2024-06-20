from django.db import models  # noqa F401


class Pokemon(models.Model):
    title_ru = models.CharField(max_length=200, default='pokemon_unnamed')
    img = models.ImageField(null=True)
    description = models.TextField(default='')
    title_en = models.CharField(max_length=200, default='')
    title_jp = models.CharField(max_length=200, default='')
    start_form = models.ForeignKey('self', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.title_ru}'


class PokemonEntity(models.Model):
    lat = models.FloatField()
    lon = models.FloatField()
    pokemon = models.ForeignKey(Pokemon, default='', on_delete=models.CASCADE)
    appeared_at = models.DateTimeField(null=True, blank=True)
    disappeared_at = models.DateTimeField(null=True, blank=True)
    level = models.IntegerField(default=1)
    health_points = models.IntegerField(default=1)
    attack_power = models.IntegerField(default=1)
    defence = models.IntegerField(default=1)
    endurance = models.IntegerField(default=1)
