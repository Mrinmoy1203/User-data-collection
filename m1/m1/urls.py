from django.contrib import admin 
from django.urls import include, path 
from demoapp import views
urlpatterns = [ 
    path('admin/', admin.site.urls), 
     path('', include('demoapp.urls')),
] 