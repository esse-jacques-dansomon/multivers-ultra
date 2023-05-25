from rest_framework import serializers

from address.serializers import CountrySerializer
from config.models import User
from developer.models import Developer, Level, Language, Experience, Status, DeveloperSkill
from skill.serializers import SkillSerializer, LevelSerializer


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class DeveloperSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    experiences = serializers.SerializerMethodField()
    languages = serializers.SerializerMethodField()
    country = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()
    developerSkills = serializers.SerializerMethodField()

    def get_country(self, obj):
        return CountrySerializer(obj.country).data

    def get_status(self, obj):
        return StatusSerializer(obj.status).data

    def get_user(self, obj):
        return UserSerializer(obj.user).data

    def get_experiences(self, obj):
        return ExperienceSerializer(obj.experiences, many=True).data

    def get_languages(self, obj):
        return LanguageSerializer(obj.languages, many=True).data

    def get_developerSkills(self, obj):
        return DeveloperSkillSerializer(obj.developer_skills, many=True).data

    class Meta:
        model = Developer
        fields = '__all__'
        extra_kwargs = {
            'cv': {'write_only': True},
            'photo': {'write_only': True},
            'video': {'write_only': True},
        }


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'


class DeveloperSkillSerializer(serializers.ModelSerializer):
    skill = SkillSerializer()
    level = LevelSerializer()

    class Meta:
        model = DeveloperSkill
        fields = '__all__'
