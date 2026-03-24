from django.contrib import admin
from django.utils.html import format_html
from .models import (
    SiteSettings,
    HeroSection,
    AboutSection,
    TeamMember,
    Newsletter,
    MembershipPlan,
    Event
)


# =========================
# 🔒 Singleton Admin Mixin
# =========================
class SingletonAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return not self.model.objects.exists()


# =========================
# 🌐 Site Settings
# =========================
@admin.register(SiteSettings)
class SiteSettingsAdmin(SingletonAdmin):
    list_display = ("site_name", "phone", "email", "logo_preview")
    readonly_fields = ("logo_preview",)

    def logo_preview(self, obj):
        if obj.logo:
            return format_html('<img src="{}" width="80" />', obj.logo.url)
        return "No Logo"
    logo_preview.short_description = "Logo"


# =========================
# 🎬 Hero Section
# =========================
@admin.register(HeroSection)
class HeroSectionAdmin(SingletonAdmin):
    list_display = ("title", "subtitle", "video_preview")
    readonly_fields = ("video_preview",)

    def video_preview(self, obj):
        if obj.video:
            return format_html(
                '<video width="120" controls><source src="{}"></video>',
                obj.video.url
            )
        return "No Video"
    video_preview.short_description = "Preview"


# =========================
# ℹ️ About Section
# =========================
@admin.register(AboutSection)
class AboutSectionAdmin(SingletonAdmin):
    list_display = ("title", "subtitle")


# =========================
# 👥 Team Members
# =========================
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


# =========================
# 📰 Newsletter
# =========================
@admin.register(Newsletter)
class NewsletterAdmin(SingletonAdmin):
    list_display = ("title",)


# =========================
# 💳 Membership Plans
# =========================
@admin.register(MembershipPlan)
class MembershipPlanAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "features_list")
    search_fields = ("name",)

    def features_list(self, obj):
        return ", ".join(obj.features)
    features_list.short_description = "Features"


# =========================
# 📅 Events
# =========================
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


from .models import HeroVideo

@admin.register(HeroVideo)
class HeroVideoAdmin(admin.ModelAdmin):
    list_display = ("title", "order", "is_active", "video_preview")
    list_editable = ("order", "is_active")

    def video_preview(self, obj):
        if obj.video:
            return format_html(
                '<video width="120" autoplay muted loop>'
                '<source src="{}"></video>',
                obj.video.url
            )
        return "No video"