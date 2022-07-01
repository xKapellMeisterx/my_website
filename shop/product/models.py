from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class ProductType(models.Model):
    type = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'тип продуктов'
        verbose_name_plural = 'Тип продукта'

    def __str__(self):
        return self.type


class Product(models.Model):
    title = models.CharField(
        'наименование продукта',
        blank=True,
        max_length=255
    )
    photo = models.ImageField(
        null=True,
        upload_to='products/',
        blank=True,
        verbose_name='фото'
    )
    description_product = models.TextField(blank=True)
    price = models.CharField(
        blank=True,
        max_length=100,
        help_text='Стоимость в рублях'
    )
    pub_date = models.DateTimeField(null=True, auto_now_add=True)
    product_type = models.ForeignKey(
        'ProductType',
        null=True,
        on_delete=models.SET_NULL
    )

    class Meta:
        ordering = ('-pub_date',)
        verbose_name = 'продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.title


class Customer(models.Model):
    name = models.CharField('имя', max_length=255, null=True)
    phone = models.CharField('номер телефона', max_length=255, null=True)
    email = models.CharField(max_length=255, null=True)
    pub_date = models.DateTimeField(null=True, auto_now_add=True)

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'Клиенты'

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS = (('Заказан', 'Заказан'),
              ('Не заказан', 'Не заказан'),
              ('В пути', 'В пути')
              )
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    customer = models.ForeignKey(
        'Customer',
        null=True,
        on_delete=models.SET_NULL
    )
    product = models.ManyToManyField('Product')

    def get_products(self):
        return '\n'.join([p.title for p in self.product.all()])

    class Meta:
        verbose_name = 'заказ'
        verbose_name_plural = 'Заказы'
