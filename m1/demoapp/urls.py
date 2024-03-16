from django.contrib import admin 
from django.urls import include, path 
from demoapp import views
urlpatterns = [ 
     path('home/', views.form_view , name='home'),
    # path('cutu/', views.cutu , name='home'),
     #path('pathview/<name>/<id>/',views.pathview,name='pathview'),
    # path('getuser/', views.qryview, name='qryview'),
#path("showform/", views.showform, name="showform"),
#path("submitform/", views.submitform, name='submitform'),
]