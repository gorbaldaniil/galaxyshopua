from django.urls import path,include
from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'checkout/$', views.checkout_view, name='checkout'),
    url(r'^change_item_qty/$', views.change_item_qty, name="change_item_qty"),
    url(r'^remove_from_cart/$', views.remove_from_cart_view, name='remove_from_cart'),
    url(r'^add_to_cart/$', views.add_to_cart_view, name='add_to_cart'),
    url(r'cart/$', views.cart_view, name='cart'),
    url(r'^product/(?P<product_slug>[-\w]+)/$', views.product_detail, name='product_view'),
    url(r'^product/(?P<product_slug>[-\w]+)/description/$', views.product_description, name='product_description'),
    url(r'^product/(?P<product_slug>[-\w]+)/video/$', views.product_video, name='product_video'),
    url(r'^product/(?P<product_slug>[-\w]+)/photos/$', views.product_photos, name='product_photos'),
    url(r'^product/(?P<product_slug>[-\w]+)/reviews/$', views.product_reviews, name='product_reviews'),
    url(r'^category/(?P<category_slug>[-\w]+)/$', views.category_detail, name='category_view'),
    url(r'^subcategory/(?P<subcategory_slug>[-\w]+)/$', views.subcategory_detail, name='subcategory_view'),
    url(r'base/', views.base, name='base'),
    path('', views.main_page, name='main_page'),
    url(r'payment/', views.payment, name="payment"),
    url(r'exchange/', views.exchange, name="exchange"),
    url(r'delivery/', views.delivery, name="delivery"),
    url(r'nightmode/', views.nightmode, name="nightmode"),
    url(r'gift/', views.gift, name="gift"),
    path('user/', views.HomePageView.as_view(), name='home'),
]