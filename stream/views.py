from django.http import StreamingHttpResponse, HttpResponse
from django.shortcuts import render
from django.views.decorators.http import condition
import time
from .models import Student


# Create your views here.
def index(request):
    res = {}
    # students = Student.objects.all()
    # res['students'] = students
    return render(request, 'index.html', res)



@condition(etag_func=None)
def indexdata(request):
    resp = StreamingHttpResponse(stream_response_generator(), )
    return resp


def indexdataajax(request):
    resp = StreamingHttpResponse(stream_response_generator(), )
    return resp

def stream_response_generator():
    students = Student.objects.all()
    yield "<html><body>\n"
    for x in students:
        yield "<div>name: %s; age: %s</div>\n" % (x.name, x.age)
    yield "</body></html>\n"


def hello(request):
    return HttpResponse("hello world")
