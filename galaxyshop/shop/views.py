from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Product, Category, CartItem, Cart
from django.urls import reverse_lazy
from django.urls import reverse
from django.http import HttpResponseRedirect, JsonResponse
from django.views import generic

from .forms import CustomUserCreationForm

class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

def base(request):
	products = Product.objects.all()
	categories = Category.objects.all()
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
		'cart' : cart
	}
	return render(request, 'shop/base.html', context)

def main_page(request):
	products = Product.objects.all()
	categories = Category.objects.all()
	context = {
		'categories': categories,
		'products': products,
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
	categories = Category.objects.all()
	context = {
		'product': product,
		'cart' : cart
	}
	return render(request, 'shop/product_detail.html', context)


def category_detail(request, category_slug):
	category = Category.objects.get(slug=category_slug)
	context = {
		'category': category
	}
	return render(request, 'shop/category_detail.html', context)

def product_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.author = request.user
            product.save()
            return redirect('product_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'shop/product_edit.html', {'form': form})

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
	context = {
		'cart' : cart
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
	return JsonResponse({ 'cart_total': cart.items.count() })

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
	return JsonResponse({ 'cart_total': cart.items.count()})

	




def payment(request):
	return render(request, 'shop/payment.html')
def exchange(request):
	return render(request, 'shop/exchange.html')
def delivery(request):
	return render(request, 'shop/delivery.html')
def shares(request):
	return render(request, 'shop/shares.html')
def basket(request):
	return render(request, 'shop/basket.html')
def comparison(request):
	return render(request, 'shop/comparison.html')
def wish_list(request):
	return render(request, 'shop/wish_list.html')
def profile(request):
	return render(request, 'shop/profile.html')


class HomePageView(TemplateView):
    template_name = 'home.html'