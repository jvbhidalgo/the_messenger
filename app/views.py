from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.


def home(request):

    users = User.objects.all().order_by('username')

    context = {'users': users}

    return render(request,'app/home.html', context)