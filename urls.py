from django.urls import path
from . import views

app_name = 'Products'

urlpatterns = [
    path('', views.product_list, name="category"),
    path('<slug:slug>/', views.product_list, name="category"),
    path('<int:id>/<slug:slug>/', views.product_detail, name="product_detail"),

]