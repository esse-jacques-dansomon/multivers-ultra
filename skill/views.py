from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from skill.models import Skill, SkillCategory
from skill.serializers import SkillSerializer, CategorySerializer, CategoryWithRelationSerializer


# Create your views here.
class SkillListView(APIView):

        # 1. GET ALL
        def get(self, request, *args, **kwargs):
            '''
            Get all skills
            '''
            Skill.objects.all()
            serializer = SkillSerializer(Skill.objects.all(), many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        # 2. CREATE ONE
        def post(self, request, *args, **kwargs):
            '''
            Create a skill
            '''
            serializer = SkillSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response("Invalid data", status=status.HTTP_400_BAD_REQUEST)


class SkillDetailView(APIView):
    def get(self, request, skill_id):
        skill = Skill.objects.get(pk=skill_id)
        serializer = SkillSerializer(skill)
        return Response(serializer.data)

    def put(self, request, skill_id):
        skill = Skill.objects.get(pk=skill_id)
        serializer = SkillSerializer(skill, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, skill_id):
        skill = Skill.objects.get(pk=skill_id)
        skill.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SkillCategoryListView(APIView):

        # 1. GET ALL
        def get(self, request, *args, **kwargs):
            '''
            Get all skills
            '''
            categories = SkillCategory.objects.all()
            serializer = CategorySerializer(categories, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        # 2. CREATE ONE
        def post(self, request, *args, **kwargs):
            '''
            Create a skill
            '''
            serializer = CategorySerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response("Invalid data", status=status.HTTP_400_BAD_REQUEST)


class SkillCategoryDetails(APIView):
    def get(self, request, pk):
        skillCategory = SkillCategory.objects.get(pk=pk)
        serializer = CategoryWithRelationSerializer(skillCategory)
        return Response(serializer.data)

    def put(self, request, pk):
        skillCategory = SkillCategory.objects.get(pk=pk)
        serializer = CategorySerializer(skillCategory, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        skillCategory = SkillCategory.objects.get(pk=pk)
        skillCategory.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)