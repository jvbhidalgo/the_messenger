from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.


def home(request):

    pesquisa = User.objects.filter(username__contains='pattern')
    users = User.objects.all().order_by('username')

    data = {}
    data['users'] = []
    for i in users:
        if i.id != request.user.id:
            data['users'].append(i)

    #context = {'users': users}

    return render(request,'app/home.html', data)