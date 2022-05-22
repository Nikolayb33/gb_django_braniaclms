from django.http import HttpResponse
# from django.shortcuts import render
# from django.views.generic import View
from django.views.generic import TemplateView
from datetime import datetime

class ContactsView(TemplateView):
    template_name = 'mainapp/contacts.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['contacts'] = [
            {
                'map':'https://yandex.ru/map-widget/v1/-/CCUAZHcrhA',
                'city':'Санкт‑Петербург',
                'phone':'+7-999-11-11111',
                'email':'geeklab@spb.ru',
                'address':'территория Петропавловская крепость, 3Ж',
            },
             {
                'map':'https://yandex.ru/map-widget/v1/-/CCUAZHX3xB',
                'city':'Казань',
                'phone':'+7-999-22-22222',
                'email':'geeklab@kz.ru',
                'address':'территория Кремль, 11, Казань, Республика Татарстан, Россия',
            },
             {
                'map':'https://yandex.ru/map-widget/v1/-/CCUAZHh9kD',
                'city':'Москва',
                'phone':'+7-999-33-33333',
                'email':'geeklab@msk.ru',
                'address':'Красная площадь, 7, Москва, Россия',
            },
        ]
        return context_data


class CoursesListView(TemplateView):
    template_name = 'mainapp/courses_list.html'


class DocSiteView(TemplateView):
    template_name = 'mainapp/doc_site.html'


class IndexView(TemplateView):
    template_name = 'mainapp/index.html'

    # def get_context_data(self, **kwargs):
    #     context_data = super().get_context_data(**kwargs)
    #     context_data['title'] = 'Приветствую путник!'
    #     return context_data


class LoginView(TemplateView):
    template_name = 'mainapp/login.html'


class NewsView(TemplateView):
    template_name = 'mainapp/news.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['object_list'] = [
            {
                'title': 'Новость раз',
                'preview': 'Превью раз',
                'date': datetime.now().strftime('%d.%m.%Y')
            },
            {
                'title': 'Новость два',
                'preview': 'Превью два',
                'date': datetime.now().strftime('%d.%m.%Y')
            },
            {
                'title': 'Новость три',
                'preview': 'Превью три',
                'date': datetime.now().strftime('%d.%m.%Y')
            },
            {
                'title': 'Новость четыре',
                'preview': 'Превью четыре',
                'date': datetime.now().strftime('%d.%m.%Y')
            },
            {
                'title': 'Новость пять',
                'preview': 'Превью пять',
                'date': datetime.now().strftime('%d.%m.%Y')
            },
            {
                'title': 'Новость шесть',
                'preview': 'Превью шесть',
                'date': datetime.now().strftime('%d.%m.%Y')
            },
        ]
        # context_data['title'] = 'Новость раз'
        # context_data['preview'] = 'Превью к новости раз'
        # context_data['date'] = '09.05.2022'
        return context_data
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
