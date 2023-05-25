from urllib.request import Request

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from skill.serializers import LevelSerializer
from .serializers import DeveloperSerializer, StatusSerializer, LanguageSerializer
from .models import Developer, Level, Status, Language


@api_view(['GET', 'POST', 'DELETE'])
def developer_list(request):
    serializer_context = {
        'request': Request(request),
    }
    if request.method == 'GET':
        developers = Developer.objects.all()
        serializer = DeveloperSerializer(developers, many=True, context=serializer_context)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = DeveloperSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        Developer.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def developer_detail(request, pk):
    try:
        developer = Developer.objects.get(pk=pk)
    except Developer.DoesNotExist:
        return Response({'error': 'Developer not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer_context = {
            'request': Request(request),
        }
        serializer = DeveloperSerializer(developer, context=serializer_context )
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = DeveloperSerializer(developer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        developer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def developer_skills(request):
    if request.method == 'GET':
        # get the developer's skills
        developer = Developer.objects.get(pk=request.user.id)
        skills = developer.skills.all()
        serializer = DeveloperSerializer(skills, many=True)


@api_view(['GET', 'POST', 'DELETE'])
def level_list(request):
    serializer_context = {
        'request': Request(request),
    }
    if request.method == 'GET':
        levels = Level.objects.all()
        serializer = LevelSerializer(levels, many=True, context=serializer_context)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = LevelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response


@api_view(['GET', 'PUT', 'DELETE'])
def status_list(request):
    if request.method == 'GET':
        status_list = Status.objects.all()
        serializer = StatusSerializer(status_list, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = StatusSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        pass


@api_view(['GET', 'PUT', 'DELETE'])
def language_list(request):
    if request.method == 'GET':
        language_list = Language.objects.all()
        serializer = LanguageSerializer(language_list, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = LanguageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        pass
