from django.db import models  # noqa F401


class Pokemon(models.Model):
    title = models.CharField(max_length=200)
    img = models.ImageField(null=True)
    description = models.TextField(default='')

    def __str__(self):
        return f'{self.title}'


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
