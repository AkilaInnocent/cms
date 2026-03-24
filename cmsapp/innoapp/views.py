from django.shortcuts import get_object_or_404, render

from .models import AboutSection, Event, HeroSection, MembershipPlan, Newsletter, SiteSettings, TeamMember


def _base_context():
    hero = HeroSection.objects.first()
    return {
        "site": SiteSettings.objects.first(),
        "hero": hero,
        "hero_words": [w.strip() for w in (hero.rotating_words if hero and hero.rotating_words else "Modern,Creative,Lifestyle").split(",") if w.strip()],
        "about": AboutSection.objects.first(),
        "newsletter": Newsletter.objects.first(),
        "members": TeamMember.objects.all(),
        "events": Event.objects.all(),
        "featured_events": Event.objects.filter(is_featured=True),
        "plans": MembershipPlan.objects.all(),
    }


def homepage(request):
    return render(request, "index.html", _base_context())


def event_list(request):
    return render(request, "index-listing.html", _base_context())


def event_detail(request, slug=None):
    context = _base_context()
    context["event"] = get_object_or_404(Event, slug=slug) if slug else Event.objects.first()
    return render(request, "index-details.html", context)
