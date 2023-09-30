from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('s/', views.subject, name='subject'),


    path('s/',include([
        path('theory/', views.theory),

    ])),

    path('pdf/', views.some_view, name='some_view'), 
] 