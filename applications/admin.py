from django.contrib import admin
from .models import Application

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('user', 'job', 'status', 'created_at')
    search_fields = ('user__email', 'job__title', 'status')
    list_filter = ('status', 'created_at')
