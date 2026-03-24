import json

from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.core.mail import send_mail
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from .models import (
    AboutSection,
    ContactMessage,
    Event,
    HeroSection,
    HeroVideo,
    MembershipPlan,
    Newsletter,
    SiteSettings,
    Solution,
    Subscriber,
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


def _get_request_data(request):
    if request.content_type == "application/json":
        try:
            return json.loads(request.body.decode("utf-8"))
        except (json.JSONDecodeError, UnicodeDecodeError):
            return None
    return request.POST


def homepage(request):
    return render(request, "index.html", _base_context())


def event_list(request):
    return render(request, "index-listing.html", _base_context())


def event_detail(request, slug=None):
    context = _base_context()
    context["event"] = get_object_or_404(Event, slug=slug) if slug else Event.objects.first()
    return render(request, "index-details.html", context)


@require_POST
def contact_submit(request):
    data = _get_request_data(request)
    if data is None:
        return JsonResponse({"status": "error", "message": "Invalid JSON payload."}, status=400)

    name = (data.get("name") or "").strip()
    email = (data.get("email") or "").strip()
    phone = (data.get("phone") or "").strip()
    message = (data.get("message") or "").strip()

    if not all([name, email, phone, message]):
        return JsonResponse({"status": "error", "message": "All fields are required."}, status=400)

    ContactMessage.objects.create(
        name=name,
        email=email,
        phone=phone,
        message=message,
    )

    send_mail(
        subject=f"New Contact from {name}",
        message=f"""
Name: {name}
Email: {email}
Phone: {phone}

Message:
{message}
""".strip(),
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[settings.EMAIL_HOST_USER],
    )

    return JsonResponse({"status": "success", "message": "Message sent successfully"})


@require_POST
def newsletter_subscribe(request):
    data = _get_request_data(request)
    if data is None:
        return JsonResponse({"status": "error", "message": "Invalid JSON payload."}, status=400)

    email = (data.get("email") or "").strip().lower()
    if not email:
        return JsonResponse({"status": "error", "message": "Email is required."}, status=400)

    _, created = Subscriber.objects.get_or_create(email=email)
    if not created:
        return JsonResponse({"status": "error", "message": "You are already subscribed"}, status=200)

    return JsonResponse({"status": "success", "message": "Subscribed successfully"})


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
