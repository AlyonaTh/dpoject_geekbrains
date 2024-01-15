from django.shortcuts import render
from django.views.generic.base import View
from .models import About


class AboutView(View):
    """About View"""
    def get(self, request):
        about = About.objects.all()
        return render(request, 'about.html', {'about': about})
