from django.http import HttpResponse


def home_page():
    return HttpResponse('<html><title>To-Do lists</title></html>')
