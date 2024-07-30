from django.shortcuts import render
from django.views import View
from courses.models import Category, Course
from teachers.models import Teacher


class IndexPage(View):
    def get(self, request):
        categories = Category.objects.all()
        teachers = Teacher.objects.all()
        courses = Course.objects.all()

        context = {
            'categories': categories,
            'teachers': teachers,
            'courses': courses,
            'active_page': 'home'
        }

        return render(request, 'blog/index.html', context)


class BaseIndexPage(View):
    def get(self, request):
        categories = Category.objects.all()
        context = {
            'categories': categories,
        }

        return render(request, 'blog/base.html', context)


class CoursesPage(View):
    def get(self, request):
        categories = Category.objects.all()
        course = Course.objects.all()

        context = {
            'categories': categories,
            'courses': course,
            'active_page': 'courses'
        }

        return render(request, 'blog/course.html', context)


class ContactPage(View):
    def get(self, request):
        context = {
            'active_page': 'contact'
        }

        return render(request, 'blog/contact.html', context)


class SinglePage(View):
    def get(self, request):
        context = {
            'active_page': 'blog'
        }

        return render(request, 'blog/single.html', context)


class AboutPage(View):
    def get(self, request):
        context = {
            'active_page': 'about'
        }

        return render(request, 'blog/about.html', context)
