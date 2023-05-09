from rest_framework import serializers
from core.models import Developer, Kind, Languages, Niveau, Skill


class DeveloperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Developer
        fields = '__all__'


class KindSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kind
        fields = '__all__'


class LanguagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Languages
        fields = '__all__'


class NiveauSerializer(serializers.ModelSerializer):
    class Meta:
        model = Niveau
        fields = '__all__'


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'
