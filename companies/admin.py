from django.contrib import admin
from .models import Company, CompanyFollower

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'website', 'created_at')
    search_fields = ('name', 'location')
    list_filter = ('created_at', 'location')


@admin.register(CompanyFollower)
class CompanyFollowerAdmin(admin.ModelAdmin):
    list_display = ('user', 'company', 'created_at')
    search_fields = ('user__email', 'company__name')
    list_filter = ('created_at',)
