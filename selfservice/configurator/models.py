from django.db import models
from autoslug import AutoSlugField
from django.core.validators import MinValueValidator, MaxValueValidator


class Crew(models.Model):
    job_title = models.CharField(max_length=255, verbose_name='Должность', help_text='Обязательное поле', editable=False)
    sort_order = models.IntegerField(verbose_name='Порядок сортировки', validators=[MaxValueValidator(1), MaxValueValidator(10)],
                                     help_text='Порядок сортировки должностей', unique=True)
    last_name = models.CharField(max_length=255, blank=True, verbose_name='Фамилия')
    first_name = models.CharField(max_length=255, blank=True, verbose_name='Имя')
    second_name = models.CharField(max_length=255, blank=True, verbose_name='Отчество')

    def __str__(self):
        return f"{self.job_title} {self.last_name} {self.first_name} {self.second_name}"

class Ship(models.Model):
    ship_name = models.CharField(max_length=255, verbose_name="Имя судна", unique=True, help_text='Обязательное поле')
    slug = AutoSlugField(populate_from='ship_name', unique=True, editable=True, verbose_name='URL')

    def __str__(self):
        return self.ship_name

class Configurator(models.Model):
    crew_member = models.ForeignKey(Crew, on_delete=models.PROTECT(), verbose_name='Член экипажа', editable=False)
    mac_address = models.TextField(verbose_name="MAC адресс телефона", help_text="Введите адресс устройства")
    phone_model = models.CharField(verbose_name='Модель телефона', )
    comments = models.TextField(blank=True, verbose_name="Комментарии")
    add_time = models.DateField(auto_now_add=True, verbose_name='Дата изменения адреса')
