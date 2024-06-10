

# Register your models here.
from django.contrib import admin
from .models import ContactSubmission, Project


# Contact us model register

@admin.register(ContactSubmission)
class ContactSubmissionAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message')
 

# Projects Model Register

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'posted_by', 'posted_date')

admin.site.register(Project, ProjectAdmin)


