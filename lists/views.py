from django.http import HttpResponse


def home_page():
    return HttpResponse('<html>')
