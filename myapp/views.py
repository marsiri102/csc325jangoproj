from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response


def home(request):
    return HttpResponse("Hello from myapp")


def about(request):
    return HttpResponse("About page")


@api_view(['GET'])
def health(request):
    return Response({"status": "ok"})