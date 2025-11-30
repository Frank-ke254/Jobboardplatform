from rest_framework import serializers
from .models import Application
from jobs.serializers import JobSerializer
from accounts.serializers import UserSerializer

class ApplicationSerializer(serializers.ModelSerializer):
    job = JobSerializer(read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = Application
        fields = ['id', 'job', 'user', 'resume_url', 'cover_letter', 'status', 'created_at']
