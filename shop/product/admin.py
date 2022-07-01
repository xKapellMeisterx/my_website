from django.contrib import admin

from product.models import Product, ProductType, Customer, Order


class ProdictAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'title',
        'description_product',
        'price',
        'pub_date',
        'product_type',
        'photo'
    )
    # list_editable = ('price',)
    search_fields = ('title',)
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'pub_date')
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('status', 'date_created', 'get_products')


@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    list_display = ('type',)


admin.site.register(Product, ProdictAdmin)

