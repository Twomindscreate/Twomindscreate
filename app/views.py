from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import ContactSubmissionForm
from django.conf import settings
from django.core.mail import send_mail
from .models import Project

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def product(request):
    return render(request, 'product.html')

def project(request):
    projects = Project.objects.all()
    return render(request,'project.html', {'projects' : projects})

def contactus(request):
    if request.method == 'POST':
        form = ContactSubmissionForm(request.POST)
        if form.is_valid():
            contact_submission = form.save()
            
            # Send confirmation email
            subject = 'Thank you for contacting us'
            message = f"Dear {contact_submission.name},\n\nThank you for reaching out to us. We have received your message and will get back to you shortly.\n\nBest regards,\nTwoMindsCreate"
            #message = f"Dear {contact_submission.name},\n\n Kajal Ji aap aapne bade dil se hame maf kahe nahi kar deti hojati he galti hamse kabhi kabhi aab mafi pane keliye kya karna hoga hame ye to bataye aap hame.  \n\nBest regards,\nAniket Suryawanshi"
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [contact_submission.email]
            
            send_mail(subject, message, from_email, recipient_list)
            
            messages.success(request, 'Your message has been successfully sent.')
            return redirect('home')
        else:
            messages.error(request, 'All fields are required')
    else:
        form = ContactSubmissionForm()
    return render(request, 'home.html', {'form': form})