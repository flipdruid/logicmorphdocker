from django.http import HttpResponse
from django.template import loader
from app.task import test_func

def landing(request):
    template = loader.get_template("main/landing.html")
    context = {}
    return HttpResponse(template.render(context, request))

def test(request):
    test_func.delay()
    return HttpResponse("Done")