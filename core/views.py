from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse

from core.models.models import Developer
from core.serializer.serializers import DeveloperSerializer


def developers_list(request):
    developers = Developer.objects.all()
    data = DeveloperSerializer(developers, many=True)
    return JsonResponse(data.data, safe=False)