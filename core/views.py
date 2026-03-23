from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods

from .models import AboutUs, ContactInfo, HeroSection, Project, Service, SocialMedia, Testimonial, VideoContent


@require_http_methods(['GET', 'POST'])
def landing_page(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        message = request.POST.get('message', '').strip()

        if name and email and message:
            send_mail(
                subject=f'Website inquiry from {name}',
                message=f'Name: {name}\nEmail: {email}\n\n{message}',
                from_email=None,
                recipient_list=[contact.email for contact in ContactInfo.objects.all() if contact.email],
                fail_silently=True,
            )
            messages.success(request, 'Thanks for reaching out. We will get back to you soon.')
        else:
            messages.error(request, 'Please fill out your name, email, and message before submitting.')
        return redirect('landing-page')

    hero = HeroSection.objects.order_by('-updated_at').first()
    services = Service.objects.all()
    videos = list(VideoContent.objects.all())
    featured_video = videos[0] if videos else None
    projects = Project.objects.all()
    testimonials = Testimonial.objects.all()
    about = AboutUs.objects.order_by('-updated_at').first()
    contact = ContactInfo.objects.order_by('-updated_at').first()
    social_links = SocialMedia.objects.all()
    project_categories = Project.objects.values_list('category', flat=True).distinct()

    context = {
        'hero': hero,
        'services': services,
        'featured_video': featured_video,
        'videos': videos,
        'projects': projects,
        'testimonials': testimonials,
        'about': about,
        'contact': contact,
        'social_links': social_links,
        'project_categories': project_categories,
    }
    return render(request, 'index.html', context)
