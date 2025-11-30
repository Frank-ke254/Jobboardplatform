from rest_framework import serializers
from .models import Company, CompanyFollower
from accounts.serializers import UserSerializer

class CompanyFollowerSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = CompanyFollower
        fields = ['user', 'created_at']

class CompanySerializer(serializers.ModelSerializer):
    followers = CompanyFollowerSerializer(source='companyfollower_set', many=True, read_only=True)
    class Meta:
        model = Company
        fields = ['id', 'name', 'description', 'website', 'logo_url', 'location', 'followers']
