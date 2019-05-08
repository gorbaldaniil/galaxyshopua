from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Product, Category, CartItem, Cart, SubCategory, Hit, ProductDescription, Description_info,Recomendations
from django.urls import reverse_lazy
from django.urls import reverse
from decimal import Decimal
from django.http import HttpResponseRedirect, JsonResponse
from django.views import generic



def base(request):
	products = Product.objects.all()
	categories = Category.objects.all()
	subcategories = SubCategory.objects.all()
	try :
		cart_id = request.session['cart_id']
		cart = Cart.objects.get(id=cart_id)
		request.session['total'] = cart.items.count()
	except:
		cart = Cart()
		cart.save()
		cart_id = cart.id
		request.session['cart_id'] = cart_id
		cart = Cart.objects.get(id=cart_id)	
	context = {
		'categories': categories,
		'products': products,
		'subcategories' : subcategories,
		'cart' : cart
	}
	return render(request, 'shop/base.html', context)

def main_page(request):
	try :
		cart_id = request.session['cart_id']
		cart = Cart.objects.get(id=cart_id)
		request.session['total'] = cart.items.count()
	except:
		cart = Cart()
		cart.save()
		cart_id = cart.id
		request.session['cart_id'] = cart_id
		cart = Cart.objects.get(id=cart_id)	

	products = Product.objects.all()
	categories = Category.objects.all()
	subcategories = SubCategory.objects.all()
	hits = Hit.objects.all()
	recomendations = Recomendations.objects.all()
	context = {
		'categories': categories,
		'products': products,
		'subcategories': subcategories,
		'hits': hits,
		'recomendations': recomendations,
		'cart' : cart
	}
	return render(request, 'shop/index.html', context)



def product_detail(request, product_slug):
	try :
		cart_id = request.session['cart_id']
		cart = Cart.objects.get(id=cart_id)
		request.session['total'] = cart.items.count()
	except:
		cart = Cart()
		cart.save()
		cart_id = cart.id
		request.session['cart_id'] = cart_id
		cart = Cart.objects.get(id=cart_id)	
	product = Product.objects.get(slug=product_slug)
	description = ProductDescription.objects.filter(product_id=product.id)
	description_info = Description_info.objects.all()
	categories = Category.objects.all()
	context = {
		'product': product,
		'cart' : cart,
		'description' : description,
		'categories' : categories,
		'description_info' : description_info
	}
	return render(request, 'shop/product_detail.html', context)

def product_description(request, product_slug):
	try :
		cart_id = request.session['cart_id']
		cart = Cart.objects.get(id=cart_id)
		request.session['total'] = cart.items.count()
	except:
		cart = Cart()
		cart.save()
		cart_id = cart.id
		request.session['cart_id'] = cart_id
		cart = Cart.objects.get(id=cart_id)	
	product = Product.objects.get(slug=product_slug)
	categories = Category.objects.all()
	# description_info = Description_info.objects.all()
	description = ProductDescription.objects.filter(product_id=product.id)
	for d in description :
		d.description_info = Description_info.objects.filter(product_description_id=d.id)
	context = {
		'categories' : categories,
		'product': product,
		'cart' : cart,
		'description' : description,
		
	}
	return render(request, 'shop/product_description.html', context)

def product_video(request, product_slug):
	try :
		cart_id = request.session['cart_id']
		cart = Cart.objects.get(id=cart_id)
		request.session['total'] = cart.items.count()
	except:
		cart = Cart()
		cart.save()
		cart_id = cart.id
		request.session['cart_id'] = cart_id
		cart = Cart.objects.get(id=cart_id)	
	product = Product.objects.get(slug=product_slug)
	categories = Category.objects.all()
	context = {
		'product': product,
		'cart' : cart,
		'categories' : categories
	}
	return render(request, 'shop/product_video.html', context)

def product_photos(request, product_slug):
	try :
		cart_id = request.session['cart_id']
		cart = Cart.objects.get(id=cart_id)
		request.session['total'] = cart.items.count()
	except:
		cart = Cart()
		cart.save()
		cart_id = cart.id
		request.session['cart_id'] = cart_id
		cart = Cart.objects.get(id=cart_id)	
	product = Product.objects.get(slug=product_slug)
	categories = Category.objects.all()
	context = {
		'product': product,
		'cart' : cart,
		'categories' : categories
	}
	return render(request, 'shop/product_photos.html', context)

def product_reviews(request, product_slug):
	try :
		cart_id = request.session['cart_id']
		cart = Cart.objects.get(id=cart_id)
		request.session['total'] = cart.items.count()
	except:
		cart = Cart()
		cart.save()
		cart_id = cart.id
		request.session['cart_id'] = cart_id
		cart = Cart.objects.get(id=cart_id)	
	product = Product.objects.get(slug=product_slug)
	categories = Category.objects.all()
	context = {
		'product': product,
		'cart' : cart,
		'categories' : categories
	}
	return render(request, 'shop/product_reviews.html', context)

def category_detail(request, category_slug):
	try :
		cart_id = request.session['cart_id']
		cart = Cart.objects.get(id=cart_id)
		request.session['total'] = cart.items.count()
	except:
		cart = Cart()
		cart.save()
		cart_id = cart.id
		request.session['cart_id'] = cart_id
		cart = Cart.objects.get(id=cart_id)	
	category = Category.objects.get(slug=category_slug)
	categories = Category.objects.all()
	subcategory = SubCategory.objects.filter(category=category.id)
	product = Product.objects.filter(category=category.id)
	context = {
		'categories': categories,
		'subcategory': subcategory,
		'product' : product,
		'cart' : cart,
		'category': category
	}
	return render(request, 'shop/category_detail.html', context)

def subcategory_detail(request, subcategory_slug):
	try :
		cart_id = request.session['cart_id']
		cart = Cart.objects.get(id=cart_id)
		request.session['total'] = cart.items.count()
	except:
		cart = Cart()
		cart.save()
		cart_id = cart.id
		request.session['cart_id'] = cart_id
		cart = Cart.objects.get(id=cart_id)	
	subcategory = SubCategory.objects.get(slug=subcategory_slug)
	categories = Category.objects.all()
	product = Product.objects.filter(subcategory_id=subcategory.id)
	context = {
		'subcategory': subcategory,
		'cart' : cart,
		'categories': categories,
		'product' : product
	}
	return render(request, 'shop/subcategory_detail.html', context)



# def product_new(request):
#     if request.method == "POST":
#         form = PostForm(request.POST)
#         if form.is_valid():
#             product = form.save(commit=False)
#             product.author = request.user
#             product.save()
#             return redirect('product_detail', pk=post.pk)
#     else:
#         form = PostForm()
#     return render(request, 'shop/product_edit.html', {'form': form})

def cart_view(request):
	try :
		cart_id = request.session['cart_id']
		cart = Cart.objects.get(id=cart_id)
		request.session['total'] = cart.items.count()
	except:
		cart = Cart()
		cart.save()
		cart_id = cart.id
		request.session['cart_id'] = cart_id
		cart = Cart.objects.get(id=cart_id)	
	categories = Category.objects.all()
	context = {
		'cart' : cart,
		'categories' : categories
	}
	return render(request, 'shop/cart.html', context)

def add_to_cart_view(request):
	try :
		cart_id = request.session['cart_id']
		cart = Cart.objects.get(id=cart_id)
		request.session['total'] = cart.items.count()
	except:
		cart = Cart()
		cart.save()
		cart_id = cart.id
		request.session['cart_id'] = cart_id
		cart = Cart.objects.get(id=cart_id)	
	product_slug = request.GET.get('product_slug')
	product = Product.objects.get(slug=product_slug)
	cart.add_to_cart(product.slug)
	new_cart_total = 0.00
	for item in cart.items.all():
		new_cart_total += float(item.item_total)
	cart.cart_total = new_cart_total
	cart.save()
	return JsonResponse({ 'cart_total': cart.items.count(), 'cart_total_price':cart.cart_total })

def remove_from_cart_view(request):
	try :
		cart_id = request.session['cart_id']
		cart = Cart.objects.get(id=cart_id)
		request.session['total'] = cart.items.count()
	except:
		cart = Cart()
		cart.save()
		cart_id = cart.id
		request.session['cart_id'] = cart_id
		cart = Cart.objects.get(id=cart_id)	
	product_slug = request.GET.get('product_slug')
	product = Product.objects.get(slug=product_slug)
	cart.remove_form_cart(product.slug)
	new_cart_total = 0.00
	for item in cart.items.all():
		new_cart_total += float(item.item_total)
	cart.cart_total = new_cart_total
	cart.save()
	return JsonResponse({ 'cart_total': cart.items.count(), 'cart_total_price':cart.cart_total})


def change_item_qty(request):
	try :
		cart_id = request.session['cart_id']
		cart = Cart.objects.get(id=cart_id)
		request.session['total'] = cart.items.count()
	except:
		cart = Cart()
		cart.save()
		cart_id = cart.id
		request.session['cart_id'] = cart_id
		cart = Cart.objects.get(id=cart_id)	
	qty = request.GET.get('qty')
	item_id = request.GET.get('item_id')
	cart_item = CartItem.objects.get(id=int(item_id))
	cart.change_qty(qty, item_id)
	return JsonResponse(
		{ 'cart_total': cart.items.count(), 
		'item_total': cart_item.item_total,
		'cart_total_price': cart.cart_total })

def checkout_view(request):
	try :
		cart_id = request.session['cart_id']
		cart = Cart.objects.get(id=cart_id)
		request.session['total'] = cart.items.count()
	except:
		cart = Cart()
		cart.save()
		cart_id = cart.id
		request.session['cart_id'] = cart_id
		cart = Cart.objects.get(id=cart_id)	
	categories = Category.objects.all()
	context = {
		'cart': cart,
		'categories' : categories
	}
	return render(request, 'shop/checkout.html', context)

def payment(request):
	try :
		cart_id = request.session['cart_id']
		cart = Cart.objects.get(id=cart_id)
		request.session['total'] = cart.items.count()
	except:
		cart = Cart()
		cart.save()
		cart_id = cart.id
		request.session['cart_id'] = cart_id
		cart = Cart.objects.get(id=cart_id)	
	categories = Category.objects.all()
	context = {
		'cart': cart,
		'categories' : categories
	}
	return render(request, 'shop/payment.html', context)

def exchange(request):
	try :
		cart_id = request.session['cart_id']
		cart = Cart.objects.get(id=cart_id)
		request.session['total'] = cart.items.count()
	except:
		cart = Cart()
		cart.save()
		cart_id = cart.id
		request.session['cart_id'] = cart_id
		cart = Cart.objects.get(id=cart_id)	
	categories = Category.objects.all()
	context = {
		'cart': cart,
		'categories' : categories
	}
	return render(request, 'shop/exchange.html', context)

def delivery(request):
	try :
		cart_id = request.session['cart_id']
		cart = Cart.objects.get(id=cart_id)
		request.session['total'] = cart.items.count()
	except:
		cart = Cart()
		cart.save()
		cart_id = cart.id
		request.session['cart_id'] = cart_id
		cart = Cart.objects.get(id=cart_id)	
	categories = Category.objects.all()
	context = {
		'cart': cart,
		'categories' : categories
	}
	return render(request, 'shop/delivery.html', context)
# def comparison(request):
# 	return render(request, 'shop/comparison.html') - розробка
# def wish_list(request):
# 	return render(request, 'shop/wish_list.html') - розробка
# def profile(request):
# 	return render(request, 'shop/profile.html') - розробка
	
def nightmode(request):
	try :
		cart_id = request.session['cart_id']
		cart = Cart.objects.get(id=cart_id)
		request.session['total'] = cart.items.count()
	except:
		cart = Cart()
		cart.save()
		cart_id = cart.id
		request.session['cart_id'] = cart_id
		cart = Cart.objects.get(id=cart_id)	
	categories = Category.objects.all()
	context = {
		'cart': cart,
		'categories' : categories
	}
	return render(request, 'shop/night-mode.html', context)

def gift(request):
	try :
		cart_id = request.session['cart_id']
		cart = Cart.objects.get(id=cart_id)
		request.session['total'] = cart.items.count()
	except:
		cart = Cart()
		cart.save()
		cart_id = cart.id
		request.session['cart_id'] = cart_id
		cart = Cart.objects.get(id=cart_id)	
	categories = Category.objects.all()
	context = {
		'cart': cart,
		'categories' : categories
	}
	return render(request, 'shop/gift.html', context)



class HomePageView(TemplateView):
    template_name = 'home.html'