from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm


def registro(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Conta criada para {username} com sucesso!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/registro.html', {'form': form})

@login_required   
def profile(request):
    return render(request, 'users/profile.html')