from rest_framework import serializers
from .models import User, Skill, AuthProvider

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['id', 'name']

class UserSerializer(serializers.ModelSerializer):
    skills = SkillSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name', 'role', 'headline', 'bio', 'location', 'profile_photo_url', 'skills']
        read_only_fields = ['role', 'created_at', 'updated_at']

class AuthProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthProvider
        fields = ['id', 'provider', 'provider_user_id']
