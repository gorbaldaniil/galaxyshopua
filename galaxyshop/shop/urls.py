from django.urls import path,include
from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^remove_from_cart/$', views.remove_from_cart_view, name='remove_from_cart'),
    url(r'^add_to_cart/$', views.add_to_cart_view, name='add_to_cart'),
    url(r'cart/$', views.cart_view, name='cart'),
    url(r'^product/(?P<product_slug>[-\w]+)/$', views.product_detail, name='product_view'),
    url(r'^category/(?P<category_slug>[-\w]+)/$', views.category_detail, name='category_view'),
    url(r'base/', views.base, name='base'),
    path('', views.main_page, name='main_page'),
    url(r'payment/', views.payment, name="payment"),
    url(r'exchange/', views.exchange, name="exchange"),
    url(r'delivery/', views.delivery, name="delivery"),
    url(r'shares/', views.shares, name="shares"),
    url(r'basket/', views.basket, name="basket"),
    url(r'comparison/', views.comparison, name="comparison"),
    url(r'wish_list/', views.wish_list, name="wish_list"),
    url(r'profile/', views.profile, name="profile"),
    path('', views.HomePageView.as_view(), name='home'),
    path('', views.SignUp.as_view(), name='signup'),


]