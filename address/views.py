from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from address.models import Country
from address.serializers import CountrySerializer


# Create your views here.

class CountryListView(APIView):

    # 1. GET ALL
    def get(self, request, *args, **kwargs):
        '''
        Get all countries
        '''
        Country.objects.all()
        serializer = CountrySerializer(Country.objects.all(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. GET ONE
    def post(self, request, *args, **kwargs):
        '''
        Create a country
        '''
        serializer = CountrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response("Invalid data", status=status.HTTP_400_BAD_REQUEST)


class CountryDetailView(APIView):
    def get_object(self, country_id):
        '''
            Helper method to get the object with given todo_id, and user_id
            '''
        try:
            return Country.objects.get(id=country_id)
        except Country.DoesNotExist:
            return None

    # 1. GET ONE
    def get(self, request, country_id, *args, **kwargs):
        '''
            Get a country
            '''
        country = self.get_object(country_id)
        serializer = CountrySerializer(country)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. GET ONE
    def put(self, request, country_id, *args, **kwargs):
        '''
            Update a country
            '''
        country = self.get_object(country_id)
        serializer = CountrySerializer(country, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response("Invalid data", status=status.HTTP_400_BAD_REQUEST)

    # 3. DELETE ONE
    def delete(self, request, country_id, *args, **kwargs):
        '''
            Delete a country
            '''
        country = self.get_object(country_id)
        if country:
            country.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)
