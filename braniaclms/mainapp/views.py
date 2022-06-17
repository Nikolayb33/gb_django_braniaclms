from django.http import HttpResponse, JsonResponse
from django.template.loader import render_to_string
from django.shortcuts import get_object_or_404
# from django.shortcuts import render
# from django.views.generic import View
from django.views.generic import TemplateView, ListView, UpdateView, DeleteView, DetailView, CreateView
from datetime import datetime
from mainapp.forms import CourseFeedbackForm
from mainapp.models import CourseFeedback
from mainapp.models import CoursesTeachers
from mainapp.models import Lesson
from mainapp.models import News
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin
from mainapp.models import Course

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


class CoursesListView(ListView):
    template_name = 'mainapp/courses_list.html'
    model = Course


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


class NewsListView(ListView):
    model = News
    paginate_by: 5
    
    def get_queryset(self):
        return super().get_queryset().filter(deleted=False)
    
class NewsDetailView(DetailView):
    model = News
    
class NewsCreateView(PermissionRequiredMixin, CreateView):
    model = News
    fields = '__all__'
    success_url = reverse_lazy('mainapp:news')
    permission_required = ('mainapp.add_news',)
    

class NewsUpdateView(PermissionRequiredMixin, UpdateView):
    model = News
    fields = '__all__'
    success_url = reverse_lazy('mainapp:news')
    permission_required = ('mainapp.change_news',)
    
class NewsDeleteView(PermissionRequiredMixin, DeleteView):
    model = News
    success_url = reverse_lazy('mainapp:news')
    permission_required = ('mainapp:delete_news')
    
class CourseDetailView(TemplateView):
    template_name = 'mainapp/course_detail.html'
    
    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['course_object'] = get_object_or_404(Course, pk=self.kwargs.get('pk'))
        context_data['lessons'] = Lesson.objects.filter(course=context_data['course_object'])
        context_data['teachers'] = CoursesTeachers.objects.filter(courses=context_data['course_object'])
        context_data['feedback_list'] = CourseFeedback.objects.filter(course=context_data['course_object'])
        
        if self.request.user.is_authenticated:
            context_data['feedback_form'] = CourseFeedbackForm(
                course=context_data['course_object'], 
                user=self.request.user)
        
        return context_data

class CourseCreateFeedbackView(CreateView):
    model = CourseFeedback
    form_class = CourseFeedbackForm
    
    def form_valid(self, form):
        self.object = form.save()
        rendered_card = render_to_string( "mainapp/includes/feedback_card.html", context={"item": self.object})
        return JsonResponse({"card": rendered_card})
    
    # def get_context_data(self, **kwargs):
    #     context_data = super().get_context_data(**kwargs)
    #     context_data['object_list'] = News.objects.all()
        # context_data['object_list'] = [
        #     {
        #         'title': 'Новость раз',
        #         'preview': 'Превью раз',
        #         'date': datetime.now().strftime('%d.%m.%Y')
        #     },
        #     {
        #         'title': 'Новость два',
        #         'preview': 'Превью два',
        #         'date': datetime.now().strftime('%d.%m.%Y')
        #     },
        #     {
        #         'title': 'Новость три',
        #         'preview': 'Превью три',
        #         'date': datetime.now().strftime('%d.%m.%Y')
        #     },
        #     {
        #         'title': 'Новость четыре',
        #         'preview': 'Превью четыре',
        #         'date': datetime.now().strftime('%d.%m.%Y')
        #     },
        #     {
        #         'title': 'Новость пять',
        #         'preview': 'Превью пять',
        #         'date': datetime.now().strftime('%d.%m.%Y')
        #     },
        #     {
        #         'title': 'Новость шесть',
        #         'preview': 'Превью шесть',
        #         'date': datetime.now().strftime('%d.%m.%Y')
        #     },
        # ]
        # context_data['title'] = 'Новость раз'
        # context_data['preview'] = 'Превью к новости раз'
        # context_data['date'] = '09.05.2022'
        # return context_data
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
