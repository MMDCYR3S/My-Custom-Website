from django.contrib import admin
from .models import Contact, WorkSamples

# Register contact admin panel
@admin.register(Contact)
class ContactAdminPanel(admin.ModelAdmin):
    list_display = ("email", "created_date")
    list_filter = ("email",)
    search_fields = ("email", "message")
    
# Register work samples admin panel
@admin.register(WorkSamples)
class WorkSamplesAdminPanel(admin.ModelAdmin):
    list_display = ("title", "status", "created_date")
    list_filter = ("title", "created_date")
    search_fields = ("title", )