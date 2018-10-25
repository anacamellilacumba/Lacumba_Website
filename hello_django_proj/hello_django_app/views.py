from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class HomePageView (TemplateView):
    template_name = "home.html"

    def get_context_data (self):
        data = { "message_title" : "Favorite Quote", "message": "Help others, even when you know they can't help you back.. ", "anonymous" : "-Anonymous"}
        return data

class ResumePageView (TemplateView):
    template_name = "resume.html"

class ContactPageView (TemplateView):
    template_name = "contact.html"