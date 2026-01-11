from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomePageView.as_view(), name="home"),
    path("about_us/", views.AboutUsView.as_view(), name="about_us"),
    path("privacy_policy/", views.PrivacyPolicy.as_view(), name="privacy_policy"),
    path("contact_us/", views.ContactUs.as_view(), name="contact_us"),
]
