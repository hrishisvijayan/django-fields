

from . import views

from django.urls import path

urlpatterns = [
    path('',views.hello,name='home'),
    path('signup/',views.signup,name='signup'),
    path('products/',views.product,name='products')
]



