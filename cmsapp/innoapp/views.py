from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect, render

from .models import (
    AboutSection,
    Event,
    HeroSection,
    HeroVideo,
    MembershipPlan,
    Newsletter,
    SiteSettings,
    Solution,
    TeamMember,
    Testimonial,
)


def _base_context():
    hero = HeroSection.objects.first()
    return {
        "site": SiteSettings.objects.first(),
        "hero": hero,
        "hero_words": [
            w.strip()
            for w in (hero.rotating_words if hero and hero.rotating_words else "Modern,Creative,Lifestyle").split(",")
            if w.strip()
        ],
        "hero_videos": HeroVideo.objects.filter(is_active=True),
        "about": AboutSection.objects.first(),
        "newsletter": Newsletter.objects.first(),
        "members": TeamMember.objects.all(),
        "events": Event.objects.all(),
        "featured_events": Event.objects.filter(is_featured=True),
        "plans": MembershipPlan.objects.all(),
        "testimonials": Testimonial.objects.filter(is_active=True),
        "solutions": Solution.objects.all(),
    }


def homepage(request):
    return render(request, "index.html", _base_context())


def event_list(request):
    return render(request, "index-listing.html", _base_context())


def event_detail(request, slug=None):
    context = _base_context()
    context["event"] = get_object_or_404(Event, slug=slug) if slug else Event.objects.first()
    return render(request, "index-details.html", context)


def contact_submit(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        send_mail(
            subject=f"New Contact from {name}",
            message=message,
            from_email=email,
            recipient_list=[settings.EMAIL_HOST_USER],
        )

        messages.success(request, "Message sent successfully")

    return redirect("homepage")


def member_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "You successfully login")
            return redirect("/admin/")

        messages.error(request, "Invalid username or password")

    return render(request, "index.html", _base_context())
