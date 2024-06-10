from django.db import models

# Create your models here.

# Contact Us Model

class ContactSubmission(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name
    
# Projects Model

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    frontend = models.CharField(max_length=100)
    backend = models.CharField(max_length=100)
    posted_date = models.DateField()
    posted_by = models.CharField( max_length=100)
    github_link = models.URLField()
    image1 = models.ImageField(upload_to='project_images/')
    image2 = models.ImageField(upload_to='project_images/')
    image3 = models.ImageField(upload_to='project_images/')

    def __str__(self):
        return self.title
    
