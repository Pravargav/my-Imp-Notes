from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('s1/', views.subject1, name='subject1'),
    path('s2/', views.subject2, name='subject2'),
    path('s3/', views.subject3, name='subject3'),
    path('s4/', views.subject4, name='subject4'),

    path('s1/',include([
        path('theory/', views.theory),
        path('radio/', views.radio),
        path('checkbox/', views.checkbox),
    ])),
    path('s2/',include([
        path('theory/', views.theory),
        path('radio/', views.radio),
        path('checkbox/', views.checkbox),
    ])),
    path('s3/',include([
        path('theory/', views.theory),
        path('radio/', views.radio),
        path('checkbox/', views.checkbox),
    ])),
    path('s4/',include([
        path('theory/', views.theory),
        path('radio/', views.radio),
        path('checkbox/', views.checkbox),
    ])),
    
    path('pdf/', views.some_view, name='some_view'),
    path('csv2/', views.some_view2, name='some_view2'),
    path('csv3/', views.some_streaming_csv_view, name='some_streaming_csv_view'),
   
    
] 