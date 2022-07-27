
from django.shortcuts import redirect, render
from . import models


# Create your views here.

def hello(request):
    a = [1,2,3,10,100,6,3,7]
    return render(request,'home.html',{"value": a})



def signup(request):
    if request.method == 'POST':
        print('hai')
        val1 = request.POST.get('name')
        val2 = request.POST.get('password')
        val3 = request.POST.get('confirm')

        if val2 == val3:
            print('hai')
            models.User.objects.create(name=val1,password=val2)
            user = models.User.objects.get(name=val1,password=val2)
            print(user)
            print(user.id)
            request.session['user_id'] = user.id
            print('session contains',request.session['user_id'])
            return redirect('home')
        else:
            error = 'password not matching'
        
    return render(request,'signup.html')


def product(request):
    product = models.Product.objects.all()
    return render(request,'products.html',{ 'product' : product })
        

