from django.http import HttpResponse


def test(request):
    return HttpResponse("This is working great")