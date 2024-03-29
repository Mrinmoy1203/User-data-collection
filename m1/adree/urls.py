from django.urls import path
from adree import views
from django.shortcuts import get_object_or_404

urlpatterns=[
    path('signup',views.SignUp.as_view()),
    path('signup/<int:pk>',views.SingleUserView.as_view()),
]