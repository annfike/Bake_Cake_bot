import jsonfield
from datetime import datetime
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField



class Customer(models.Model):
    external_id = models.PositiveIntegerField(
        verbose_name='Внешний ID покупателя',
        unique=True,
    )
    tg_username = models.CharField('Имя покупателя в Телеграме',
        max_length=50, blank=True, default='')
    first_name = models.CharField('Имя',
        max_length=256, blank=True, default='')
    last_name = models.CharField('Фамилия',
        max_length=256, blank=True, default='')
    phone_number = PhoneNumberField()
    GDPR_status = models.BooleanField(null=True, default=False)
    home_address = models.CharField('Домашний адрес',
        max_length=50, blank=True, default='')

    def __str__(self):
        return f'{self.first_name} ({self.external_id})'

    class Meta:
        verbose_name = 'Покупатель'
        verbose_name_plural = 'Покупатели'


class Product(models.Model):
    product_name = models.CharField(max_length=256)

    def __str__(self):
        return f'{self.product_name}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

class Product_properties(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    property_name = models.CharField(max_length=256)

    def __str__(self):
        return f'{self.property_name}'

    class Meta:
        verbose_name = 'Свойства Продукта'
        verbose_name_plural = 'Свойства Продуктов'

class Product_parameters(models.Model):
    product_property = models.ForeignKey(Product_properties, verbose_name='Свойства Продукта', on_delete=models.CASCADE)
    parameter_name = models.CharField(verbose_name='Название параметра', max_length=256)
    parameter_price = models.PositiveIntegerField(
        verbose_name='Цена',
    )

    class Meta:
        verbose_name = 'Параметры продукта'
        verbose_name_plural = 'Параметры продуктов'

class Order(models.Model):
    order_number = models.PositiveIntegerField("Номер заказа", null=True, default=None, unique=True)
    customer = models.CharField(verbose_name='Имя Покупателя', null=True, blank=True,
        max_length=256)
    customer_chat_id = models.CharField(verbose_name='Chat ID Покупателя', null=True, blank=True,
    max_length=256)
    order_details = jsonfield.JSONField(verbose_name='Детали заказа', default='Пока нет ничего')
    order_price  = models.PositiveIntegerField(
        verbose_name='Цена заказа',
    )
    Processing = 'Заявка обрабатывается'
    Cooking = 'Готовим ваш торт'
    Transport = 'Продукт в пути'
    Delivered = 'Продукт у вас'
    order_statuses = [
        (Processing, 'Заявка обрабатывается'),
        (Cooking, 'Готовим ваш торт'),
        (Transport, 'Продукт в пути'),
        (Delivered, 'Продукт у вас'),
    ]
    order_status = models.CharField(verbose_name='Статус заказа',
        max_length=256,
        choices=order_statuses,
        default=Processing,
    )
    comments = models.CharField(verbose_name='Комментарии', null=True, blank=True,
        max_length=256)
    # delivery_address = models.CharField(verbose_name='Адрес доставки',
    #     max_length=256, default=' ')
    # delivery_date = models.DateField(verbose_name='Дата доставки', null=True, blank=True)
    # delivery_time = models.TimeField(verbose_name='Время доставки', null=True, blank=True)

    # def __str__(self):
    #     return self.delivery_time.isoformat(timespec='minutes')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'