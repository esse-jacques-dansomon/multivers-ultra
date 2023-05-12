from rest_framework import serializers

from developer.models import Developer, Level, Language


class DeveloperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Developer
        fields = '__all__'
        extra_kwargs = {
            'cv': {'write_only': True},
            'photo': {'write_only': True},
            'video': {'write_only': True},
        }


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = '__all__'


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'