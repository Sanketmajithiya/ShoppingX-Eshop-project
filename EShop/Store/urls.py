from django.urls import path
from .views.home import Home,Index,ProfileView,changepassword,address,clear_cache
from .views.signup import Signup
from .views.login import Login,logout,forgot_password,verify_otp,reset_password,resend_otp
from .views.cart import Cart,update_cart,remove_from_cart
from .views.checkout import CheckOut,PaymentSuccess
from .views.orders import OrderView
from .views.home import ProfileView 
from .middlewares.auth import auth_middleware

urlpatterns = [
  path('',Home.as_view(),name='home'),
  path('homepage',Index.as_view(),name='homepage'),
  path('signup',Signup.as_view(), name='signup'),
  path('login',Login.as_view(), name='login'),
  path('logout',logout, name='logout'),
  path('cart',Cart.as_view(), name='cart'),
  path('update-cart/', update_cart, name='update_cart'),
  path('remove-from-cart/', remove_from_cart, name='remove_from_cart'),
  path('check-out',CheckOut.as_view(),name='checkout'),
  path('Orders',auth_middleware(OrderView.as_view()),name='Orders'),
  path('profile',ProfileView.as_view(), name='profile'),
  path('address',address, name='address'),
  path('changepassword',changepassword, name='changepassword'),
  # path('checkout/',CheckOut.as_view(), name='checkout'),
  path('payment-success/',PaymentSuccess.as_view(),name='payment_success'),
  path('forgot-password/',forgot_password,name='forgotpassword'),
  path('verify-otp/', verify_otp, name='verify_otp'),
  path('resend-otp/', resend_otp, name='resend_otp'),
  path('reset-password/', reset_password, name='reset_password'),
  path('clear_cache/',clear_cache,name='clear_cache'),
]



























# path('send-test-email/', send_test_email, name='send_test_email'),

# path('passwordchage/',passwordchangeView.as_view(template_name='passwordchange.html',from_class=MyPasswordchangeForm,success_url='/passwordchangedone/'),
# name='passwordchage'),

# path('passwordchagedone/',passwordchangeView.as_view(template_name='passwordchange.html'),name='passwordchangedone')

# path('send_email',send_email,name='send_email')
  