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



import io
from django.http import FileResponse
from reportlab.pdfgen import canvas

def some_view(request):
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer)
    p.drawString(10, 10, "Hello world.")
    p.showPage()
    p.save()
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='hello.pdf')




