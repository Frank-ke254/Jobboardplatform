from django.db import models
from accounts.models import User

class Company(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    website = models.CharField(max_length=255, blank=True)
    logo_url = models.TextField(blank=True)
    location = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    followers = models.ManyToManyField(User, through='CompanyFollower', related_name='followed_companies', blank=True)

    def __str__(self):
        return self.name

class CompanyFollower(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'company')

    def __str__(self):
        return f"{self.user.email} follows {self.company.name}"
