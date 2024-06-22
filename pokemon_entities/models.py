from django.db import models  # noqa F401


class Pokemon(models.Model):
    title_ru = models.CharField(max_length=200, verbose_name='Название (рус)')
    img = models.ImageField(null=True, verbose_name='Картинка')
    description = models.TextField(verbose_name='Описание', blank=True)
    title_en = models.CharField(max_length=200, verbose_name='Название (англ)', blank=True)
    title_jp = models.CharField(max_length=200, verbose_name='Название (япон)', blank=True)
    previous_evolution = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True,
                                           related_name='next_evolutions', verbose_name='Предыдущая ступень эволюции')

    def __str__(self):
        return self.title_ru


class PokemonEntity(models.Model):
    lat = models.FloatField(verbose_name='Широта')
    lon = models.FloatField(verbose_name='Долгота')
    pokemon = models.ForeignKey(Pokemon, default='покемон не указан', on_delete=models.CASCADE,
                                verbose_name='Укажите покемона', related_name='pokemon_entities')
    appeared_at = models.DateTimeField(blank=True, null=True, verbose_name='Время появления на карте')
    disappeared_at = models.DateTimeField(blank=True, null=True, verbose_name='Время появления на карте')
    level = models.IntegerField(blank=True, verbose_name='Уровень', null=True)
    health_points = models.IntegerField(blank=True, verbose_name='Очки здоровья', null=True)
    attack_power = models.IntegerField(blank=True, verbose_name='Сила атаки', null=True)
    defence = models.IntegerField(blank=True, verbose_name='Защита', null=True)
    endurance = models.IntegerField(blank=True, verbose_name='Выносливость', null=True)

    def __str__(self):
        return f'{self.pokemon} уровень {self.level}'
