from django.shortcuts import render

def index(request):
    context={}
    return render(request, 'takeTest/index.html', context)

def subject(request):
    context={}
    return render(request, 'takeTest/subject.html', context)

def theory(request):
    context={}
    return render(request, 'takeTest/theory.html', context)
