from django.shortcuts import render
from .models import Product, Category

def base(request):
	products = Product.objects.all()
	categories = Category.objects.all()
	context = {
		'categories': categories,
		'products': products
	}
	return render(request, 'shop/base.html', context)

def main_page(request):
	products = Product.objects.all()
	categories = Category.objects.all()
	context = {
		'categories': categories,
		'products': products
	}
	return render(request, 'shop/index.html', context)

def product_detail(request, pk):
	product = get_object_or_404(Product, pk=pk)
	return render(request, 'shop/product_detail.html', {'product': product})

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
