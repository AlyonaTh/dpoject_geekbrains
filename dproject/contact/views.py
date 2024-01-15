from django.shortcuts import render, redirect
from django.views.generic.base import View
from .models import Contact
from .form import ContactForm


class ContactView(View):
    def get(self, request):
        contact = Contact.objects.all()
        return render(request, 'contact.html', {'contact': contact})


class SendMessage(View):
    """Send Message"""

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            form = form.save()
        return redirect('/contact/')