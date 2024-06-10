from django import forms
from .models import ContactSubmission, Project


# Contact us Form

class ContactSubmissionForm(forms.ModelForm):
    class Meta:
        model = ContactSubmission
        fields = ['name', 'email', 'message']


# Projects List Form

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'frontend', 'backend', 'posted_date', 'posted_by', 'github_link', 'image1', 'image2', 'image3']