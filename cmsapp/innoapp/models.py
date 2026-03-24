from django.db import models


class SiteSettings(models.Model):
    site_name = models.CharField(max_length=120, default="Tiya Golf Club")
    logo = models.ImageField(upload_to="site/", blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, default="010-020-0340")
    email = models.EmailField(blank=True, default="info@company.com")
    address = models.CharField(max_length=255, blank=True, default="London, United Kingdom")
    footer_text = models.CharField(max_length=255, blank=True, default="Copyright © 2048 Tiya Golf Club")
    working_hours_weekday = models.CharField(max_length=100, blank=True, default="6:00 AM - 6:00 PM")
    working_hours_weekend = models.CharField(max_length=100, blank=True, default="6:30 AM - 8:30 PM")

    def __str__(self):
        return self.site_name


class HeroSection(models.Model):
    title = models.CharField(max_length=150, default="Welcome to the club")
    subtitle = models.CharField(max_length=150, default="Tiya is")
    rotating_words = models.CharField(max_length=255, default="Modern,Creative,Lifestyle")
    video_url = models.URLField(blank=True, default="https://www.youtube.com/embed/MGNgbNGOzh8")
    button_text_1 = models.CharField(max_length=100, default="Our Story")
    button_link_1 = models.CharField(max_length=255, default="#section_2")
    button_text_2 = models.CharField(max_length=100, default="Become a member")
    button_link_2 = models.CharField(max_length=255, default="#section_3")

    def __str__(self):
        return self.title


class AboutSection(models.Model):
    title = models.CharField(max_length=150, default="About Tiya")
    subtitle = models.CharField(max_length=150, default="Tiya Club History")
    description_1 = models.TextField(default="Since 1984, Tiya is ranked #8 in the top 10 golf courses in the world.")
    description_2 = models.TextField(default="Tiya Golf Club is 100% free CSS template provided by TemplateMo website.")

    def __str__(self):
        return self.title


class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    image = models.ImageField(upload_to="team/", blank=True, null=True)
    twitter = models.URLField(blank=True)
    whatsapp = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)

    def __str__(self):
        return f"{self.name} - {self.role}"


class Newsletter(models.Model):
    title = models.CharField(max_length=150, default="Get our newsletter")
    description = models.TextField(default="Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor ut labore et dolore.")

    def __str__(self):
        return self.title


class MembershipPlan(models.Model):
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=50)
    features = models.JSONField(default=list, blank=True)

    def __str__(self):
        return f"{self.name} ({self.price})"


class Event(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    image = models.ImageField(upload_to="events/", blank=True, null=True)
    date = models.DateField()
    location = models.CharField(max_length=150)
    price = models.CharField(max_length=50, default="$0")
    is_featured = models.BooleanField(default=False)
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ["date"]

    def __str__(self):
        return self.title
