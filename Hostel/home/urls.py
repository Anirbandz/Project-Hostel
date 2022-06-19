from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name = 'home'),
    path("about", views.about, name = 'about'),
    path("contact_us", views.contact_us, name = 'contact_us'),
    path("pricing", views.pricing, name = 'pricing'),
    path("login", views.login, name = 'login'),
    path("logout", views.handlelogout, name = 'handlelogout'),
    path("register", views.register, name = 'register'),
    path("meal", views.meal, name = 'meal'),
    path("payment", views.payment, name = 'payment'),
    path("gallary", views.gallary, name = 'gallary'),
    path("info", views.info, name = 'info'),
    path("extra", views.extra, name = 'extra'),
    path("infra", views.infra, name = 'infra'),
    path("care", views.care, name = 'care'),
    path("form", views.form, name = 'form'),
    path("tc", views.tc, name = 'tc'),
    path("hostel_more", views.hostel_more, name = 'hostel_more')
]