from django.db import models  # noqa F401


class Pokemon(models.Model):
    title_ru = models.CharField(max_length=200, default='pokemon_unnamed', verbose_name='Название (рус)')
    img = models.ImageField(null=True, verbose_name='Картинка')
    description = models.TextField(default='описание покемона', verbose_name='Описание')
    title_en = models.CharField(max_length=200, default='название покемона на английском',
                                verbose_name='Название (англ)')
    title_jp = models.CharField(max_length=200, default='название покемона на японском', verbose_name='Название (япон)')
    previous_evolution = models.ForeignKey('self', on_delete=models.CASCADE, null=True,
                                           related_name='next_evolution', verbose_name='Предыдущая ступень эволюции')

    def __str__(self):
        return f'{self.title_ru}'


class PokemonEntity(models.Model):
    lat = models.FloatField(verbose_name='Широта')
    lon = models.FloatField(verbose_name='Долгота')
    pokemon = models.ForeignKey(Pokemon, default='ссылка на модель покемона', on_delete=models.CASCADE,
                                verbose_name='Укажите покемона')
    appeared_at = models.DateTimeField(null=True, blank=True, verbose_name='Время появления на карте')
    disappeared_at = models.DateTimeField(null=True, blank=True, verbose_name='Время появления на карте')
    level = models.IntegerField(default=1, verbose_name='Уровень покемона')
    health_points = models.IntegerField(default=1, verbose_name='Очки здоровья')
    attack_power = models.IntegerField(default=1, verbose_name='Сила атаки')
    defence = models.IntegerField(default=1, verbose_name='Защита')
    endurance = models.IntegerField(default=1, verbose_name='Выносливость')
