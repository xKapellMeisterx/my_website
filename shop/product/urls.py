from django.urls import path
from product import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path(
        'category/<slug:slug>/',
        views.category_product,
        name='category_product'
    ),
    path('profile/<str:username>', views.profile),

]
