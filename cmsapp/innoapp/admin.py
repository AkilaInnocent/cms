from django.contrib import admin

from .models import AboutSection, Event, HeroSection, MembershipPlan, Newsletter, SiteSettings, TeamMember


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ("site_name", "phone", "email")


@admin.register(HeroSection)
class HeroSectionAdmin(admin.ModelAdmin):
    list_display = ("title", "subtitle")


@admin.register(AboutSection)
class AboutSectionAdmin(admin.ModelAdmin):
    list_display = ("title", "subtitle")


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ("name", "role")


@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ("title",)


@admin.register(MembershipPlan)
class MembershipPlanAdmin(admin.ModelAdmin):
    list_display = ("name", "price")


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("title", "date", "location", "price", "is_featured")
    prepopulated_fields = {"slug": ("title",)}
