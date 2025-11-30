from rest_framework import viewsets
from .models import Job
from .serializers import JobSerializer
from .filters import JobFilter
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django_filters.rest_framework import DjangoFilterBackend


class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.select_related('company').all()
    serializer_class = JobSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = JobFilter
    filterset_fields = ("location", "category")
    permission_classes = [IsAdminUser]

    
