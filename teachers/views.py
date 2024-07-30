from django.shortcuts import render
from django.views import View

# Create your views here.


class TeachersPage(View):
    def get(self, request):
        context = {
            'active_page': 'teachers'
        }

        return render(request, 'blog/teacher.html', context)
