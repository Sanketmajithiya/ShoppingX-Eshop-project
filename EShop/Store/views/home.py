from django.shortcuts import render, redirect, HttpResponse
from Store.models.product import Product
from Store.models.category import Category
from Store.models.customer import Customer
from django.core.paginator import Paginator
from django.views import View
from Store.forms import *
from django.core.cache import cache
from django.contrib import messages


# Create your views here.
class Index(View):
    def post(self, request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')

        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity <= 1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity - 1
                else:
                    cart[product] = quantity + 1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart
        return redirect(request.META.get('HTTP_REFERER'))

    def get(self, request):
        if not request.session.get('customer'):
            messages.warning(request, "please login or register to continue shopping")
        cart = request.session.get('cart', {})  
        Category_id = request.GET.get('category')

        if Category_id == "all":
            request.session.pop('selected_category', None)
            Category_id = None
        elif Category_id and not Category_id.isdigit():
            print("Category filter received:", Category_id)
            category_obj = Category.objects.filter(Name__icontains=Category_id).first()
            if category_obj:
                request.session['selected_category'] = category_obj.Name
                Category_id = category_obj.id
            else:
                Category_id = None
                request.session.pop('selected_category', None)
        elif Category_id and Category_id.isdigit():
            category_obj = Category.objects.filter(id=Category_id).first()
            if category_obj:
                request.session['selected_category'] = category_obj.Name

        else:
            Category_id = None

        # Caching categories
        categories = cache.get('categories', None)
        if not categories:
            categories = Category.get_all_categories()
            cache.set('categories', categories, timeout=300)

        search_query = request.GET.get('search')
        price_query = None

        if search_query and search_query.isdigit():
            price_query = float(search_query)

        cache_key = f'products_{Category_id}_{search_query}_{price_query}'
        products = cache.get(cache_key)

        if not products:
            if Category_id:
                products = Product.get_all_products_by_categoryid(int(Category_id))
            elif price_query is not None:
                products = Product.objects.filter(Price__lte=price_query).order_by('id')
            elif search_query:
                products = Product.objects.filter(Name__icontains=search_query).order_by('id')
            else:
                products = Product.get_all_products().order_by('id')

            cache.set(cache_key, products, timeout=300)

        paginator = Paginator(products, 6)
        page_number = request.GET.get('page')
        paginated_products = paginator.get_page(page_number)

        data = {
            'products': paginated_products,
            'categories': categories,
            'selected_category': request.session.get('selected_category'),
            'search_query': search_query,
        }

        return render(request, 'index.html', data)



def clear_cache(request):
    try:
        cache.set('categories', Category.get_all_categories(), timeout=300)
        cache.set('home_products', Product.get_all_products(), timeout=300)
        cache.clear()

        print("Cache cleared successfully")
        return HttpResponse("Cache has been cleared successfully")
    except Exception as e:
        print(f"Error during cache clearing: {e}")
        return HttpResponse(f"An error occurred: {e}", status=500)


class ProfileView(View):
    def get(self, request):
        email = request.session.get('email')
        
        # Store selected category to session (for navbar highlight)
        category = request.GET.get('category')
        if category:
            request.session['selected_category'] = category
        else:
            request.session['selected_category'] = None

        try:
            user = Customer.objects.get(Email=email)
            first_name = user.First_Name
            request.session['first_name'] = first_name  # Also set this if not already
        except Customer.DoesNotExist:
            first_name = "Guest"

        return render(request, 'profile.html', {'first_name': first_name})
    
    def post(self, request):
        return self.get(request)


# class ProfileView(View):
#     def get(self, request):
#         email = request.session.get('email')
#         try:
#             user = Customer.objects.get(Email=email)
#             first_name = user.First_Name
#         except Customer.DoesNotExist:
#             first_name = "Guest"

#         return render(request, 'profile.html', {'first_name': first_name})


def address(request):
    return render(request, 'address.html')


# class Home(View):
#     def get(self, request):
#         category = request.GET.get('category')
#         if category:
#             request.session['selected_category'] = category  

#         products = cache.get('home_products')
#         if not products:
#             products = Product.get_all_products()
#             cache.set('home_products', products, timeout=300)

#         return render(request, 'home.html', {
#             'products': products,
#             'selected_category': request.session.get('selected_category', ''),
#             'range': range(1, 13)
#         })

class Home(View):
    def get(self, request):
        category = request.GET.get('category')
        if category:
            request.session['selected_category'] = category

        products = cache.get('home_products')
        if not products:
            products = Product.get_all_products()
            cache.set('home_products', products, timeout=300)

        # ✅ Add this list for payment option images
        pay_options = ['cc', 'upi', 'nb', 'bj']

        return render(request, 'home.html', {
            'products': products,
            'selected_category': request.session.get('selected_category', ''),
            'range': range(1, 13),
            'pay_options': pay_options,  # ✅ Passed to template
        })



def changepassword(request):
    if request.method == 'POST':
        form = MyPasswordchangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            return redirect('password_change_done')
    else:
        form = MyPasswordchangeForm(request.user)

    return render(request, 'changepassword.html', {'form': form})





# old code Index it's Working 

# Create your views here.
# class Index(View):
#    def post(self,request):
#       product = request.POST.get('product')
#       remove = request.POST.get('remove')
#       cart = request.session.get('cart')
#       if cart:
#         quantity = cart.get(product)
#         if quantity: 
#            if remove:
#                if quantity<=1:
#                   cart.pop(product)
#                else:   
#                  cart[product] = quantity-1
#            else:
#                cart[product] = quantity+1  
#         else:
#            cart[product] = 1
#       else:
#         cart = {}
#         cart[product] = 1
#       request.session['cart'] = cart
#       print('cart', request.session['cart'])
#       return redirect(request.META.get('HTTP_REFERER')) 

#    def get(self, request):
#     cart = request.session.get('cart', {})
#     Category_id = request.GET.get('category')
#     # Caching categories
#     categories = cache.get('categories', None)
#     if not categories:
#         categories = Category.get_all_categories()
#         cache.set('categories', categories, timeout=300)  # Cache categories for 5 minutes

#     products = []
#     search_query = request.GET.get('search')
#     Category_id = request.GET.get('category')
#     price_query = None

#     if search_query and search_query.isdigit(): 
#         price_query = float(search_query)

#     cache_key = f'products_{Category_id}_{search_query}_{price_query}'

#     products = cache.get(cache_key)

#     if not products:  # If products are not in cache, fetch them from DB
#         if Category_id:
#             Category_id = int(Category_id)
#             products = Product.get_all_products_by_categoryid(Category_id)
#         elif price_query is not None:
#             products = Product.objects.filter(Price__lte=price_query).order_by('id')
#         elif search_query:
#             products = Product.objects.filter(Name__icontains=search_query).order_by('id')
#         else:
#             products = Product.get_all_products().order_by('id')

#         cache.set(cache_key, products, timeout=300)  

#     # Pagination logic 
#     paginator = Paginator(products, 6)  
#     page_number = request.GET.get('page')  
#     paginated_products = paginator.get_page(page_number)

#     data = {
#         'products': paginated_products,
#         'categories': categories,
#         'selected_category': Category_id,
#         'search_query': search_query,
#     }
#     print("Session data:", request.session.items())
#     print('Logged in user email:', request.session.get('email'))
    
#     return render(request, 'index.html', data)










