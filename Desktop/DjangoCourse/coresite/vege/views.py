from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.

# Logic for adding receipe to the list
def add_receipe(request):
    if request.method == "POST":
        data = request.POST

        receipe_image = request.FILES.get('receipe_image')
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')

        # print(receipe_name)
        # print(receipe_description)
        # print(receipe_image)

        Receipe.objects.create(
            receipe_name = receipe_name,
            receipe_description = receipe_description,
            receipe_image = receipe_image,
        )

        return redirect('/view-all/')

    
    
    return render(request, 'add_receipe.html')


# Logic for deleting receipe from the list
def delete_receipe(request, id):
    query_set = Receipe.objects.get(id = id)
    query_set.delete()

    return redirect('/update-receipe/')


# Logic for updating individual item of the list
def update_item(request, id):
    query_set = Receipe.objects.get(id = id)

    context = {'receipe': query_set}

    if request.method == 'POST':
        data = request.POST

        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')
        receipe_image = request.FILES.get('receipe_image')


        query_set.receipe_name = receipe_name
        query_set.receipe_description = receipe_description

        if receipe_image:
            query_set.receipe_image = receipe_image

        query_set.save()
        return redirect('/view-all/')


    

    return render(request, 'update_item.html', context)


# Logic for viewing all item from the list
def view_all(request):

    receipe_list = Receipe.objects.all()

    if request.GET.get('search'):
        receipe_list = Receipe.objects.filter(receipe_name__icontains = request.GET.get('search'))

    context = {'receipes': receipe_list}

    return render(request, 'view_all.html', context)


# Logic for viewing items for making an action.
def update_receipe(request):
    receipe_list = Receipe.objects.all()

    if request.GET.get('search'):
        receipe_list = Receipe.objects.filter(receipe_name__icontains = request.GET.get('search'))

    context = {'receipes': receipe_list}

    return render(request, 'update_receipe.html', context)

# login form for user
def login(request):

    return render(request, 'login.html')


# signup form for user
def signup(request):
    if request.method == 'POST':

        # collecting information from form and storing in a variable
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        # checking if username already exist or not...
        user = User.objects.filter(username = username)

        if user.exists():
            messages.info(request, 'Sorry! username is already taken.')
            return redirect('/signup/')


        # Creating user object 
        user = User.objects.create(
            first_name = first_name,
            last_name = last_name,
            username = username
        )

        # encrypting password
        user.set_password(password)

        # save created object
        user.save()
        messages.info(request, 'Account Created Successfully.')
        return redirect('/signup/')

    return render(request, 'signup.html')