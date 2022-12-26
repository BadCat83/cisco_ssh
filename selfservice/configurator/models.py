from django.db import models
from autoslug import AutoSlugField
from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator


class JobTitle(models.Model):
    job_title = models.CharField(max_length=255, verbose_name='Должность')
    sort_order = models.IntegerField(verbose_name='Порядок сортировки',
                                     validators=[MinValueValidator(1), MaxValueValidator(14)],
                                     help_text='Порядок сортировки должностей', unique=True)
    slug = AutoSlugField(populate_from='job_title', unique=True, editable=True,
                         verbose_name='URL')

    def __str__(self):
        return f"{self.job_title}"

    class Meta:
        verbose_name = "Должность"
        verbose_name_plural = "Должности"
        ordering = ['sort_order']

class Crew(models.Model):
    job_title = models.ForeignKey(JobTitle, on_delete=models.PROTECT)
    last_name = models.CharField(max_length=255, blank=True, verbose_name='Фамилия')
    first_name = models.CharField(max_length=255, blank=True, verbose_name='Имя')
    second_name = models.CharField(max_length=255, blank=True, verbose_name='Отчество')
    ship = models.ForeignKey('Ships', on_delete=models.PROTECT, verbose_name='Судно',
                             help_text='Обязательное поле')

    def __str__(self):
        return f"{self.job_title} {self.last_name} {self.first_name} {self.second_name}"

    class Meta:
        verbose_name = "Член экипажа"
        verbose_name_plural = "Члены экипажа"

class Ships(models.Model):
    ship_name = models.CharField(max_length=255, verbose_name="Имя судна", unique=True,
                                 help_text='Обязательное поле')
    router_ip = models.GenericIPAddressField(protocol='ipv4', unique=True)
    slug = AutoSlugField(populate_from='ship_name', unique=True, editable=True,
                         verbose_name='URL')

    def __str__(self):
        return self.ship_name

    class Meta:
        verbose_name = 'Судно'
        verbose_name_plural = 'Суда'
        ordering = ['ship_name']

class Configurator(models.Model):
    crew_member = models.ForeignKey(Crew, on_delete=models.PROTECT,
                                    verbose_name='Член экипажа', unique=True)
    mac_address = models.CharField(max_length=12, validators=(MinLengthValidator(12),),
                                   verbose_name="MAC адресс телефона",
                                   help_text="Введите адресс устройства", unique=True)
    phone_model = models.CharField(max_length=255, verbose_name='Модель телефона', blank=True)
    comments = models.TextField(blank=True, verbose_name="Комментарии")
    add_time = models.DateField(auto_now_add=True, verbose_name='Дата изменения адреса')

    class Meta:
        verbose_name = "MAC адрес"
        verbose_name_plural = "MAC адреса"