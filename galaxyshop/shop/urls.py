from django.urls import path,include
from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'base/', views.base, name='base'),
    path('', views.main_page, name='main_page'),
    url(r'^product/(?P<pk>[0-9]+)/$', views.product_detail, name='product_detail'),
    url(r'payment/', views.payment, name="payment"),
    url(r'exchange/', views.exchange, name="exchange"),
    url(r'delivery/', views.delivery, name="delivery"),
    url(r'shares/', views.shares, name="shares"),
    url(r'basket/', views.basket, name="basket"),
    url(r'comparison/', views.comparison, name="comparison"),
    url(r'wish_list/', views.wish_list, name="wish_list"),
    url(r'profile/', views.profile, name="profile"),
]