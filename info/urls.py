from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("blog/", views.blog, name="blog"),
    path("contact/", views.contact, name="contact"),
    path("umar_naveed/", views.umar_naveed, name="umar_naveed"),
    path("team/", views.team, name="team"),
    path("services/", views.services, name="services"),
    # path("", views.home, name="home"),
]