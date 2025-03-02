from django.shortcuts import render,redirect
from item.models import Category,Item

from .forms import SignupForm
from django.contrib.auth import logout
from django.contrib import messages
def index(request):
    items= Item.objects.filter(is_sold=False)[0:6]
    categories= Category.objects.all()

    return render(request,'myapp/index.html',{
        'categories':categories,
        'items':items,
    })
    
def contact(request):
    return render(request,'myapp/contact.html')

def signup(request):
    if request.method=='POST':
        form=SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form=SignupForm()
    return render(request,'myapp/signup.html',{
        'form':form,
    })

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        messages.success(request, "You have been logged out successfully!")
        return redirect('myapp:index')
    return render(request, 'myapp/logout.html')