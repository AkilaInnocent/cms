from django.contrib import admin

from .models import AboutUs, ContactInfo, HeroSection, Project, Service, SocialMedia, Testimonial, VideoContent


@admin.register(HeroSection)
class HeroSectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'call_to_action_text', 'updated_at')
    search_fields = ('title', 'subtitle', 'call_to_action_text')


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'display_order', 'updated_at')
    list_editable = ('display_order',)
    search_fields = ('title', 'description', 'icon')


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'featured', 'created_at')
    list_filter = ('category', 'featured')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'description', 'category')


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'rating', 'created_at')
    list_filter = ('rating',)
    search_fields = ('name', 'message')


@admin.register(VideoContent)
class VideoContentAdmin(admin.ModelAdmin):
    list_display = ('title', 'display_order', 'updated_at')
    list_editable = ('display_order',)
    search_fields = ('title', 'video_url')


@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('headline', 'updated_at')
    search_fields = ('headline', 'content')


@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ('email', 'phone', 'business_hours', 'updated_at')
    search_fields = ('email', 'phone', 'address', 'business_hours')


@admin.register(SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ('platform_name', 'display_order', 'url')
    list_editable = ('display_order',)
    search_fields = ('platform_name', 'icon_class', 'url')
