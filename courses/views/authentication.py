from django.shortcuts import render
from django.views import View


class AuthenticationView(View):
    def get(self, request):
        return render(request, 'blog/auth.html')
