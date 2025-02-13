from .forms import CVForm 
from .models import CV 
from django.shortcuts import render, redirect
from .forms import ContactForm  # Ensure the form is imported
from django.core.mail import send_mail 
from django.shortcuts import get_object_or_404, redirect 
from django.contrib import messages 
from django.conf import settings 


def contact_view(request):
    form = ContactForm()  # Ensure 'form' is always initialized

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Saves to the database
            return redirect('success_page')  # Ensure 'success_page' exists in urls.py

    return render(request, 'contact.html', {'form': form})


def success_view(request):
    return render(request, 'success.html')  # Render the success page


def create_cv(request): 
    if request.method == "POST": 
        form = CVForm(request.POST, request.FILES)  # Handle file uploads 
        if form.is_valid(): 
            form.save() 
            return redirect('cv_list')  # Redirect to CV listing page 
    else:
        form = CVForm() 
    return render(request, 'cv_form.html', {'form': form}) 


def cv_list_view(request):
    cvs = CV.objects.all()
    for cv in cvs:
        print(f"CV Name: {cv.name}, CV ID: {cv.id}")  # Debugging output
    return render(request, 'cv_list.html', {'cvs': cvs})


def share_cv_email(request, cv_id): 
    cv = get_object_or_404(CV, id=cv_id) 
    recipient_email = request.POST.get('email') 
    if recipient_email: 
        subject = f"{cv.name}'s CV" 
        message = f"Check out {cv.name}'s CV at {request.build_absolute_uri(cv.profile_picture.url)}" 
        sender_email = settings.EMAIL_HOST_USER 
        send_mail(subject, message, sender_email, [recipient_email]) 
        messages.success(request, "CV shared successfully via email.") 
    else: 
        messages.error(request, "Please provide a valid email.") 
    return redirect('cv_list') 

