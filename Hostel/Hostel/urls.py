from django.contrib import admin
from django.urls import path
from django.urls.conf import include

admin.site.site_header = "User Admin"
admin.site.site_title = "User Admin Portal"
admin.site.index_title = "Welcome to User Admin Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls'))
]
