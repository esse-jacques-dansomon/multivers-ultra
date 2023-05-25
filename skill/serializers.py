from rest_framework import serializers

from developer.models import Level
from skill.models import SkillCategory, Skill


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SkillCategory
        fields = '__all__'


class SkillSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Skill
        fields = '__all__'
