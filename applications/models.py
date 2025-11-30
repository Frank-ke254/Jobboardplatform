from django.db import models
from jobs.models import Job
from accounts.models import User

class Application(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applications')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='applications')
    resume_url = models.TextField(blank=True)
    cover_letter = models.TextField(blank=True)
    status = models.CharField(max_length=50, default='submitted')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('job', 'user')

    def __str__(self):
        return f"{self.user.email} applied to {self.job.title}"
