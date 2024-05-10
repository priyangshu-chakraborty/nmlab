from django.shortcuts import render,redirect,get_object_or_404
from .models import User

# Create your views here.
def user_list(request):
    users=User.objects.all()
    return render(request,'myapp/user.html',{"users":users})

def add_user(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        User.objects.create(username=username,password=password)
        return redirect('user')
    return render(request,"myapp/register.html")

def delete_user(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    if request.method == "POST":
        user.delete()
        return redirect('user')
    return render(request, 'myapp/delete_user.html', {'user': user})

