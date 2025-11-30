from django.db import models
from companies.models import Company
from accounts.models import User

class Job(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='jobs')
    category = models.CharField(max_length=100, blank=True, db_index=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    requirements = models.TextField(blank=True)
    employment_type = models.CharField(max_length=50, blank=True)
    location = models.CharField(max_length=255, blank=True, db_index=True)
    salary_range = models.CharField(max_length=255, blank=True)
    remote = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    saved_by = models.ManyToManyField(User, through='SavedJob', related_name='saved_jobs', blank=True)

    def __str__(self):
        return f"{self.title} at {self.company.name}"
    

    class Meta:
        indexes = [
            models.Index(fields=['location']),
            models.Index(fields=['category']),
        ]


class SavedJob(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    saved_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'job')

    def __str__(self):
        return f"{self.user.email} saved {self.job.title}"
