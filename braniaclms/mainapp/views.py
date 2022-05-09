from django.http import HttpResponse
# from django.shortcuts import render
# from django.views.generic import View
from django.views.generic import TemplateView


class ContactsView(TemplateView):
    template_name = 'mainapp/contacts.html'


class CoursesListView(TemplateView):
    template_name = 'mainapp/courses_list.html'


class DocSiteView(TemplateView):
    template_name = 'mainapp/doc_site.html'


class IndexView(TemplateView):
    template_name = 'mainapp/index.html'


class LoginView(TemplateView):
    template_name = 'mainapp/login.html'


class NewsView(TemplateView):
    template_name = 'mainapp/news.html'
# Create your views here.
# def hello_world(request):
#     return HttpResponse("Hello_world!")

# class HelloWorld(View):
#     def get(self, request, *args, **kwargs):
#         return HttpResponse('Hello World!')

# def blog(request):
#     return HttpResponse("I'am blog")

# def blog(request, **kwargs):
#     return HttpResponse(f'{kwargs}')    
