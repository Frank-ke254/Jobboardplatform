from rest_framework import serializers
from .models import Job, SavedJob
from companies.models import Company
from accounts.serializers import UserSerializer

class SavedJobSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = SavedJob
        fields = ['user', 'saved_at']

class JobSerializer(serializers.ModelSerializer):
    company = serializers.PrimaryKeyRelatedField(
        queryset=Company.objects.all()
    )

    saved_by = SavedJobSerializer(source='savedjob_set', many=True, read_only=True)

    class Meta:
        model = Job
        fields = [
            'id',
            'company',
            'category',
            'title',
            'description',
            'requirements',
            'employment_type',
            'location',
            'salary_range',
            'remote',
            'saved_by',
            'created_at',
            'updated_at'
        ]
