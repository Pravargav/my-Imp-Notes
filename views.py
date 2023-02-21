
from django.shortcuts import render,HttpResponse
from django.shortcuts import get_object_or_404

def index(request):
    context={}
    return render(request, 'takeTest/index.html', context)

def subject1(request):
    context={}
    return render(request, 'takeTest/subject1.html', context)

def subject2(request):
    context={}
    return render(request, 'takeTest/subject2.html', context)

def subject3(request):
    context={}
    return render(request, 'takeTest/subject3.html', context)

def subject4(request):
    context={}
    return render(request, 'takeTest/subject4.html', context)

def theory(request):
    context={}
    return render(request, 'takeTest/theory.html', context)

def radio(request):
    context={}
    return render(request, 'takeTest/radio.html', context)

def checkbox(request):
    context={}
    return render(request, 'takeTest/checkbox.html', context)

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

import csv
from django.http import HttpResponse

def some_view2(request):
    response = HttpResponse(
        content_type='text/csv',
        headers={'Content-Disposition': 'attachment; filename="somefilename.csv"'},
    )

    writer = csv.writer(response)
    writer.writerow(['First row', 'Foo', 'Bar', 'Baz'])
    writer.writerow(['Second row', 'A', 'B', 'C', '"Testing"', "Here's a quote"])

    return response

import csv
from django.http import StreamingHttpResponse

class Echo:
   
    def write(self, value):
        return value

def some_streaming_csv_view(request):

    rows = (["Row {}".format(idx), str(idx)] for idx in range(65536))
    pseudo_buffer = Echo()
    writer = csv.writer(pseudo_buffer)
    return StreamingHttpResponse(
        (writer.writerow(row) for row in rows),
        content_type="text/csv",
        headers={'Content-Disposition': 'attachment; filename="somefilename.csv"'},
    )


