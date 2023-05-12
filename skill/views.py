from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from skill.models import Skill
from skill.serializers import SkillSerializer


# Create your views here.
class SkillCreateView(APIView):
    def post(self, request):
        serializer = SkillSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        skills = Skill.objects.all()
        serializer = SkillSerializer(skills, many=True)
        return Response(serializer.data)

    def put(self, request):
        skill = Skill.objects.get(pk=request.data['id'])
        serializer = SkillSerializer(skill, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        skill = Skill.objects.get(pk=request.data['id'])
        skill.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def getSkillByCategory(self, request, category):
        skills = Skill.objects.filter(category=category)
        serializer = SkillSerializer(skills, many=True)
        return Response(serializer.data)