from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactSubmissionForm
from django.conf import settings
from django.core.mail import send_mail, EmailMultiAlternatives
from .models import Project

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def product(request):
    return render(request, 'product.html')

def project(request):
    projects = Project.objects.all()
    return render(request, 'project.html', {'projects': projects})

def contactus(request):
    if request.method == 'POST':
        form = ContactSubmissionForm(request.POST)
        if form.is_valid():
            contact_submission = form.save()

            # Send confirmation email
            subject = 'Thank you for contacting us'
            message = f"""Dear {contact_submission.name},

Thank you for reaching out to us. We have received your message and will get back to you shortly.

We offer Web Development Website services at INR 7900.

Included:
1. 4 Pages Website
2. Responsive Design
3. Mobile Friendly Layout
4. Website will be ready in 2 - 3 days
5. 1 Business Email ID
6. Domain + Server
7. Outlook Email Configuration

Additional Services:
1. Logo Design
2. Desktop Application Development

For more info, please contact: twomindscreate17@gmail.com

Best regards,
TwoMindsCreate
"""
            html_message = f"""
                <html>
                <body>
                    <p>Dear {contact_submission.name},</p>
                    <p>Thank you for reaching out to us. We have received your message and will get back to you shortly.</p>
                    <p>We offer Web Development Website services at INR 7900.</p>
                    <p>Included:</p>
                    <ul>
                        <li>4 Pages Website</li>
                        <li>Responsive Design</li>
                        <li>Mobile Friendly Layout</li>
                        <li>Website will be ready in 2 - 3 days</li>
                        <li>1 Business Email ID</li>
                        <li>Domain + Server</li>
                        <li>Outlook Email Configuration</li>
                    </ul>
                    <p>Additional Services:</p>
                    <ul>
                        <li>Logo Design</li>
                        <li>Desktop Application Development</li>
                    </ul>
                    <p>For more info, please contact: <a href="mailto:twomindscreate17@gmail.com">twomindscreate17@gmail.com</a></p>
                    <p>Best regards,</p>
                    <p>TwoMindsCreate</p>
                </body>
                </html>
            """

            from_email = settings.EMAIL_HOST_USER
            recipient_list = [contact_submission.email]

            email = EmailMultiAlternatives(subject, message, from_email, recipient_list)
            email.attach_alternative(html_message, "text/html")
            email.send()

            messages.success(request, 'Your message has been successfully sent.')
            return redirect('home')
        else:
            messages.error(request, 'All fields are required.')
    else:
        form = ContactSubmissionForm()
    return render(request, 'contact.html', {'form': form})
