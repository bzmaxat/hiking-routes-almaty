from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog, Difficulty
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User, AnonymousUser
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .forms import BlogForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required


class Diffs:
    """"""
    def get_diffs(self):
        return Difficulty.objects.all()


class BlogsView(Diffs, ListView):
    """Список маршрутов"""
    model = Blog
    queryset = Blog.objects.all()


class BlogDetailView(Diffs, DetailView):
    """Полное описание маршрута"""
    model = Blog
    slug_field = "url"


class MyBlogsView(Diffs, ListView):
    """Мои маршруты"""
    def get_queryset(self):
        queryset = Blog.objects.filter(user=self.request.user)
        return queryset


def signupuser(request):
    if request.method == 'GET':
        return render(request, 'blog/signupuser.html', {'form': UserCreationForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('blog_list')
            except IntegrityError:
                return render(request, 'blog/signupuser.html',
                              {'form': UserCreationForm, 'error': 'Имя пользователя уже занято'})
        else:
            return render(request, 'blog/signupuser.html', {'form': UserCreationForm, 'error': 'Пароли не совпадают'})


def loginuser(request):
    if request.method == 'GET':
        return render(request, 'blog/loginuser.html', {'form': AuthenticationForm})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'blog/loginuser.html', {'form': AuthenticationForm, 'error': 'Неверное сочетание: логин, пароль'})
        else:
            login(request, user)
            return redirect('blog_list')


def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('blog_list')


@login_required
def createblog(request):
    if request.method == 'GET':
        return render(request, 'blog/createblog.html', {'form': BlogForm()})
    else:
        try:
            form = BlogForm(request.POST, request.FILES)
            newblog = form.save(commit=False)
            newblog.user = request.user
            newblog.save()
            return redirect('blog_list')
        except ValueError:
            return render(request, 'blog/createblog.html',
                          {'form': BlogForm(), 'error': 'Bad data passed in. Try again.'})


class FilterBlogsView(Diffs, ListView):
    """Фильтр маршрутов"""
    def get_queryset(self):
        queryset = Blog.objects.filter(difficulty__in=self.request.GET.getlist('diff'))
        return queryset
