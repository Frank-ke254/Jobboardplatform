from django.contrib import admin
from .models import Job, SavedJob

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'employment_type', 'location', 'remote', 'created_at')
    search_fields = ('title', 'company__name', 'employment_type', 'location')
    list_filter = ('employment_type', 'remote', 'created_at')
    list_select_related = ('company',)  # improves performance for FK lookups


@admin.register(SavedJob)
class SavedJobAdmin(admin.ModelAdmin):
    list_display = ('user', 'job', 'saved_at')
    search_fields = ('user__email', 'job__title')
    list_filter = ('saved_at',)
    list_select_related = ('user', 'job')
