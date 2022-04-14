from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from monitor.forms import CreateCustomUserForm, LoginCustomUserForm, CreateHostForm

# home_menu = {'home': 'Главная',
#              'events': 'События',
#              'reports': 'Отчеты',
#              'host_list': 'Список хостов',
#              'settings': 'Настройки',
#              'about': 'Справка',
#              }
from monitor.models import Host

home_menu = {'up': {
                 'home': 'Главная',
                 'events': 'События',
                 'reports': 'Отчеты',
                 'host_list': 'Список хостов',
                 'settings': 'Настройки',
                },
            'down': {
                 'profile': 'Профиль',
                 'about': 'Справка',
                 'logout': 'Выйти'
                }
            }


def login(request):
    context = {
        'title': 'Авторизация',
    }
    return render(request, 'monitor/login.html', context=context)


def home(request):
    context = {
        'title': 'Главная',
        'menu': home_menu
    }
    return render(request, 'monitor/home.html', context=context)


def events(request):
    context = {
        'title': 'События',
        'menu': home_menu
    }
    return render(request, 'monitor/events.html', context=context)


def reports(request):
    context = {
        'title': 'Отчеты',
        'menu': home_menu
    }
    return render(request, 'monitor/reports.html', context=context)


def host_list(request):
    context = {
        'title': 'Список хостов',
        'menu': home_menu
    }
    return render(request, 'monitor/host_list.html', context=context)


def settings(request):
    context = {
        'title': 'Настройки',
        'menu': home_menu
    }
    return render(request, 'monitor/settings.html', context=context)


def about(request):
    context = {
        'title': 'Справка',
        'menu': home_menu
    }
    return render(request, 'monitor/about.html', context=context)


def profile(request):
    context = {
        'title': 'Профиль пользователя',
        'menu': home_menu
    }
    return render(request, 'monitor/profile.html', context=context)


def edit_host(request):
    pass


class CreateHost(CreateView):
    form_class = CreateHostForm
    template_name = 'monitor/create_host.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = home_menu
        context['title'] = 'Создание хоста'
        return context


class RegisterUser(CreateView):
    """
    Создание нового пользователя в системе
    """
    form_class = CreateCustomUserForm
    template_name = 'monitor/register_user.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = home_menu
        context['title'] = 'Создание пользователя'
        return context


class LoginUser(LoginView):
    form_class = LoginCustomUserForm
    template_name = 'monitor/login.html'

    def get_success_url(self):
        return reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Вход'
        return context


class HostList(ListView):
    model = Host
    template_name = 'monitor/host_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Список хостов'
        context['menu'] = home_menu
        return context


def logout_user(request):
    logout(request)
    return redirect('login')