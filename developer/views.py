from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from developer.models import Developer
from developer.serializers import DeveloperSerializer


class DeveloperCreateView(APIView):
    def post(self, request, format=None):
        serializer = DeveloperSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):
        developers = Developer.objects.all()
        serializer = DeveloperSerializer(developers, many=True)
        return Response(serializer.data)

    def put(self, request, format=None):
        developer = Developer.objects.get(pk=request.data['id'])
        serializer = DeveloperSerializer(developer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, format=None):
        developer = Developer.objects.get(pk=request.data['id'])
        developer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

