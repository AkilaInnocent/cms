from django.contrib import admin
from django.utils.html import format_html

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


class SingletonAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return not self.model.objects.exists()


@admin.register(SiteSettings)
class SiteSettingsAdmin(SingletonAdmin):
    list_display = ("site_name", "phone", "email", "logo_preview")
    readonly_fields = ("logo_preview",)

    def logo_preview(self, obj):
        if obj.logo:
            return format_html('<img src="{}" width="80" />', obj.logo.url)
        return "No Logo"

    logo_preview.short_description = "Logo"


@admin.register(HeroSection)
class HeroSectionAdmin(SingletonAdmin):
    list_display = ("title", "subtitle", "video_preview")
    readonly_fields = ("video_preview",)

    def video_preview(self, obj):
        if obj.video:
            return format_html('<video width="120" controls><source src="{}"></video>', obj.video.url)
        return "No Video"

    video_preview.short_description = "Preview"


@admin.register(AboutSection)
class AboutSectionAdmin(SingletonAdmin):
    list_display = ("title", "subtitle")


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ("name", "role", "image_preview")
    search_fields = ("name", "role")
    readonly_fields = ("image_preview",)

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="60" />', obj.image.url)
        return "No Image"

    image_preview.short_description = "Photo"


@admin.register(Newsletter)
class NewsletterAdmin(SingletonAdmin):
    list_display = ("title",)


@admin.register(MembershipPlan)
class MembershipPlanAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "features_list")
    search_fields = ("name",)

    def features_list(self, obj):
        return ", ".join(obj.features)

    features_list.short_description = "Features"


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("title", "date", "location", "price", "is_featured", "image_preview")
    list_filter = ("date", "is_featured")
    search_fields = ("title", "location")
    prepopulated_fields = {"slug": ("title",)}
    readonly_fields = ("image_preview",)
    date_hierarchy = "date"

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="80" />', obj.image.url)
        return "No Image"

    image_preview.short_description = "Banner"


@admin.register(HeroVideo)
class HeroVideoAdmin(admin.ModelAdmin):
    list_display = ("title", "order", "is_active", "video_preview")
    list_editable = ("order", "is_active")

    def video_preview(self, obj):
        if obj.video:
            return format_html(
                '<video width="120" autoplay muted loop><source src="{}"></video>',
                obj.video.url,
            )
        return "No video"


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ("name", "role", "rating", "link", "is_active")
    list_filter = ("is_active", "rating")
    search_fields = ("name", "role", "message", "link")
    list_editable = ("is_active", "rating")
    ordering = ("-rating",)


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "created_at")
    search_fields = ("name", "email", "message")
    readonly_fields = ("name", "email", "phone", "message", "created_at")


@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ("email", "created_at")
    search_fields = ("email",)
    readonly_fields = ("email", "created_at")


@admin.register(Solution)
class SolutionAdmin(admin.ModelAdmin):
    list_display = ("title",)
    search_fields = ("title", "description")
    ordering = ("title",)
