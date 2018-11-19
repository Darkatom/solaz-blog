from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, reverse

from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm

def login(request):
    if request.user.groups.filter(name="Editor").exists():
        return  HttpResponseRedirect(reverse('blog:dashboard_posts'))

    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = request.POST['username']
            password = request.POST['password']
            access = auth.authenticate(username=user, password=password)
            if access is not None and access.is_active:
                auth.login(request, access)
                return  HttpResponseRedirect(reverse('blog:dashboard_posts'))
        else:
            context = { 'form': form } 
            return render(request, 'blog/users/login.html', context)

    context = { 'form': AuthenticationForm() } 
    return render(request, 'blog/users/login.html', context)

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('blog:index'))