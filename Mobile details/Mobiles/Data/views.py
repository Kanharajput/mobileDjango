from django.shortcuts import render
from .models import Info

# Create your views here.


def home(request):
    return render(request, 'home.html') 



def search(request):
    query1 = request.GET['ram']
    query2 = request.GET['rom']
    sear_phone = Info.objects.filter(RAM__icontains=query1)
    return render(request, "show.html",{'sear': sear_phone})