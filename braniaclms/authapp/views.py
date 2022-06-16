from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, UpdateView
from django.contrib import messages
from authapp.models import User
from django.urls import reverse, reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView

from authapp.forms import CustomUserCreationForm, CustomUserChangeForm

# Create your views here.


class CustomLoginView(LoginView):
    template_name = 'authapp/login.html'
    extra_context = {
        'title':'Вход пользователя'
    }


class RegisterView(CreateView):
    model = User
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('mainapp:index')
    # template_name = 'authapp/register.html'


# class RegisterView(TemplateView):
#     template_name = 'authapp/register.html'
#     extra_context = {
#         'title':'Регистрация пользователя'
#     }

#     def post(self, request, **kwargs):
#         try:
#             print(type(request.POST)) 
#             if all(
#                 (
#                     request.POST.get('username'),
#                     request.POST.get('email'),
#                     request.POST.get('password1'),
#                     request.POST.get('password2'),
#                     request.POST.get('first_name'),
#                     request.POST.get('last_name'),
#                     request.POST.get('password1') == request.POST.get('password2'),
                    
#                 )
#             ):
#                 new_user = User.objects.create(
#                     username=request.POST.get('username'),
#                     first_name=request.POST.get('first_name'),
#                     last_name=request.POST.get('last_name'),
#                     email=request.POST.get('email'),
#                     age=request.POST.get('age') if request.POST.get('age') else 0,
#                     avatar=request.FILES.get('avatar'),
#                 )
#                 new_user.set_password(request.POST.get('password1'))
#                 new_user.save()
#                 messages.add_message(request, messages.INFO, 'Регистрация прошла успешно')
#                 return HttpResponseRedirect(reverse('authapp:login'))
#             else:
#                 messages.add_message(
#                     request,
#                     messages.INFO, 
#                     'Что-то пошло не так'
#                 )
#                 return HttpResponseRedirect(reverse('authapp:register'))
#         except Exception as e:
#             messages.add_message(
#                 request,
#                 messages.INFO, 
#                 'Что-то пошло не так'
#             )
#             return HttpResponseRedirect(reverse('authapp:register'))
        
#         # return HttpResponseRedirect(reverse('authapp:login'))


class CustomLogoutView(LogoutView):
    pass


class EditView(UpdateView):
    model = User
    form_class = CustomUserChangeForm
    
    template_name = 'authapp/edit.html'
    
    def get_object(self, queryset=None):
        return self.request.user
    
    def get_success_url(self):
        return reverse_lazy('authapp:edit', args=[self.request.user.pk])
    # extra_context = {
    #     'title': 'Регистрация пользователя'
    # }

    # def post(self, request, **kwargs):
    #     if request.POST.get('username'):
    #         request.user.username = request.POST.get('username')

    #     if request.POST.get('first_name'):
    #         request.user.first_name = request.POST.get('first_name')

    #     if request.POST.get('last_name'):
    #         request.user.last_name = request.POST.get('last_name')

    #     if request.POST.get('age'):
    #         request.user.age = request.POST.get('age')

    #     if request.POST.get('password'):
    #         request.user.set_password(request.POST.get('password'))

    #     request.user.save()
    #     return HttpResponseRedirect(reverse('authapp:edit'))


