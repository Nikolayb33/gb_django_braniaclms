from curses.ascii import NUL
from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings

NULLABLE =  {'blank':True, 'null':True}


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата последненго изменения')

    deleted = models.BooleanField(default=False, verbose_name='Удален')

    class Meta:
        abstract = True
        ordering = ('-created_at',)


class NewsManager(models.Manager):
    
    def delete(self):
        pass

    def get_queryset(self):
        return super().get_queryset(deleted=False)


class News(BaseModel):
    objects = NewsManager

    title = models.CharField(max_length=255, verbose_name='Заголовок')
    preamble = models.CharField(max_length=1000, verbose_name='Вступление')
    body = models.TextField(verbose_name='Содержимое')
    body_as_markdown = models.BooleanField(default=False, verbose_name='Способ разметки')

    def __str__(self):
        return f'#{self.pk} {self.title}'
    
    class Meta:
        verbose_name = 'новость'
        verbose_name_plural = 'новости'

    def delete(self, *args, **kwargs):
        self.deleted = True
        self.save()
    

class Course(BaseModel):
    name = models.CharField(max_length=256, verbose_name='main')
    description = models.TextField(verbose_name='Description', **NULLABLE)
    description_at_mark_down = models.BooleanField(verbose_name='As markdown', default=False)
    cost = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Cost', default=0)
    cover = models.CharField(max_length=25, default='no_image.svg', verbose_name='Cover')

    def __str__(self):
        return f'{self.pk} {self.name}'

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'
# Create your models here.


class Lesson(BaseModel):
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    num = models.PositiveIntegerField(verbose_name='Lesson number')
    title = models.CharField(max_length=256, verbose_name='Name')
    description = models.TextField(verbose_name='Description', **NULLABLE)
    description_as_markdown = models.BooleanField(verbose_name='As_markdown', default=False)

    def __str__(self):
        return f'{self.course.name} | {self.num} | {self.title}'

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'
        ordering = ('course', 'num',)


class CoursesTeachers(BaseModel):
    courses = models.ManyToManyField(Course)
    name_first = models.CharField(max_length=128, verbose_name='Name')
    name_second = models.CharField(max_length=128, verbose_name='Surname')
    day_birth = models.DateField(verbose_name='Birth date')

    def __str__(self):
        return '{0:0>3} {1} {2}'.format(
            self.pk, self.name_second, self.name_first
        )


class CourseFeedback(BaseModel):
    
    RATINGS = (
        (5, '⭐⭐⭐⭐⭐'),
        (4, '⭐⭐⭐⭐'),
        (3, '⭐⭐⭐'),
        (2, '⭐⭐'),
        (1, '⭐'),
    )
    
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Курс')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь')
    rating = models.SmallIntegerField(choices=RATINGS, default=5, verbose_name='Рейтинг')
    feedback = models.TextField(verbose_name='Отзыв', default='Без отзыва')
    
    class Meta:
        verbose_name = ''
        verbose_name_plural = ''
    
    def __str__(self):
        return f'Отзыв на {self.course} от {self.user}'
    
