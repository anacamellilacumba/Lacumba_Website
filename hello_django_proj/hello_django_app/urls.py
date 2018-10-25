from django.urls import path
from .views import HomePageView, ResumePageView, ContactPageView

urlpatterns = [
    path('home/', HomePageView.as_view(), name="home_view"),
    path('resume/', ResumePageView.as_view(), name="resume_view"),
    path('contact/', ContactPageView.as_view(), name="contact_view")

]