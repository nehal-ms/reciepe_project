from django.shortcuts import render,redirect
from .models import *
from django.db.models import Q 
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/register/')
def reciepes (request):
    if request.method == "POST":
        
        data = request.POST 
    #print(data) 
        Reciepe_name = data.get('Reciepe_name')
        Reciepe_description = data.get('Reciepe_description')
        Reciepe_image= request.FILES.get('Reciepe_image')
        
        
        print(Reciepe_name)
        print(Reciepe_description)
        print(Reciepe_image)

        Reciepe.objects.create(
            Reciepe_name = Reciepe_name,
            Reciepe_description = Reciepe_description,
            Reciepe_image = Reciepe_image   )
        
        return redirect('/reciepes/')
    
    
    queryset = Reciepe.objects.all()

    if request.GET.get('search'):
        print(request.GET.get('search'))    

        queryset = queryset.filter(Q(Reciepe_description__icontains = request.GET.get('search')) | 
                                   Q(Reciepe_name__icontains = request.GET.get('search')))

        
        #queryset = queryset.filter(Reciepe_description__icontains = request.GET.get('search'))
        #queryset = queryset.filter(Reciepe_name__icontains = request.GET.get('search'))
        #return render(request, 'reciepe.html', context)
        


    context = {'reciepes':queryset}
    return render (request,'reciepes.html',context)

def update_reciepe(request,id):
    queryset = Reciepe.objects.get(id=id)

    if request.method == "POST":
        data = request.POST
        
        Reciepe_name = data.get('Reciepe_name')
        Reciepe_description = data.get('Reciepe_description')
        Reciepe_image= request.FILES.get('Reciepe_image')
        
        queryset.Reciepe_name = Reciepe_name
        queryset.Reciepe_description = Reciepe_description

        if Reciepe_image:
            queryset.Reciepe_image = Reciepe_image

        queryset.save()
        return redirect('/reciepes/')





    context = {'recipe':queryset}
    return render (request, 'update_recipe.html',context)


def delete_reciepe(request,id):
    queryset = Reciepe.objects.get(id=id)
    queryset.delete()
    return redirect('/reciepes/')

def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.info(request, "Invalid Username")
            return redirect('/login/')
        
        user = authenticate(username = username,password = password)

        if user is None:
            messages.info(request, "Invalid Password")
            return redirect('/login/')
        
        else:
            login(request,user)
            return redirect('/reciepes/')
        

    
    
    return render(request, 'login.html')

def register_page(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username = username)

        if user.exists():
            messages.info(request, "Username Already Exists.")
            return redirect('/register/')
        


        user = User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username,
            password=password)

        user.set_password(password)
        user.save()
        messages.info(request, "Account Created Successfully")


        return redirect('/register/')
        
        
    return render(request, 'register.html')



    
