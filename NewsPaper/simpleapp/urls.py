from django.urls import path , include
# Импортируем созданное нами представление
from .views import NewsList, NewDetail, ProductsList, multiply, ProductsCreate, ProductsDetail, ProductsUpdate, \
   ProductsDelete, NewsCreate, NewsDelete, NewsUpdate




urlpatterns = [
   path('news/', NewsList.as_view()),

   # pk — это первичный ключ товара, который будет выводиться у нас в шаблон
   # int — указывает на то, что принимаются только целочисленные значения
   path('news/<int:pk>', NewDetail.as_view()),
   path('products/', ProductsList.as_view()),
   path('multiply/', multiply),
   path('create/', ProductsCreate.as_view(), name='product_create'),
   path('<int:pk>/update/', ProductsUpdate.as_view(), name='product_update'),
   path('<int:pk>/delete/', ProductsDelete.as_view(), name='product_delete'),
   path('news/create/', NewsCreate.as_view(), name='post_create'),
   path('news/update/', NewsUpdate.as_view(), name='post_update'),
   path('news/delete/', NewsDelete.as_view(), name='post_delete'),
   path("accounts/", include("allauth.urls")),
]
