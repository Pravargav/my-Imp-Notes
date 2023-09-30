from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('subject/', views.subject, name='subject'),


    path('subject/',include([
        path('theory/', views.theory),

    ])),

    path('pdf/', views.some_view, name='some_view'), 
] 
