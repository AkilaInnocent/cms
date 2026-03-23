from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.text import slugify


class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class HeroSection(TimestampedModel):
    title = models.CharField(max_length=200)
    subtitle = models.TextField()
    background_image = models.ImageField(upload_to='hero/')
    call_to_action_text = models.CharField(max_length=80)
    call_to_action_link = models.CharField(max_length=200, help_text='Use an internal anchor like #contact or a full URL.')

    class Meta:
        verbose_name = 'Hero section'
        verbose_name_plural = 'Hero sections'

    def __str__(self):
        return self.title


class Service(TimestampedModel):
    title = models.CharField(max_length=150)
    description = models.TextField()
    icon = models.CharField(max_length=80, blank=True, help_text='Optional Bootstrap Icons class, e.g. bi bi-hammer.')
    image = models.ImageField(upload_to='services/')
    display_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['display_order', 'title']

    def __str__(self):
        return self.title


class ProjectCategory(models.TextChoices):
    CONSTRUCTION = 'construction', 'Construction'
    MASONRY = 'masonry', 'Masonry'
    CRAFTSMANSHIP = 'craftsmanship', 'Craftsmanship'
    HOME_CRAFTS = 'home-crafts', 'Home Crafts'
    WATER_REPAIR = 'water-repair', 'Water Repair'
    PLUMBING = 'plumbing', 'Plumbing Construction'


class Project(TimestampedModel):
    title = models.CharField(max_length=150)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    video_url = models.URLField(blank=True)
    category = models.CharField(max_length=40, choices=ProjectCategory.choices)
    slug = models.SlugField(max_length=170, blank=True, unique=True)
    featured = models.BooleanField(default=False)

    class Meta:
        ordering = ['-featured', '-created_at']

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1
            while Project.objects.exclude(pk=self.pk).filter(slug=slug).exists():
                counter += 1
                slug = f'{base_slug}-{counter}'
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Testimonial(TimestampedModel):
    name = models.CharField(max_length=120)
    message = models.TextField()
    rating = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    image = models.ImageField(upload_to='testimonials/', blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.name} ({self.rating}/5)'


class VideoContent(TimestampedModel):
    title = models.CharField(max_length=150)
    video_url = models.URLField()
    thumbnail = models.ImageField(upload_to='videos/thumbnails/')
    display_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['display_order', 'title']
        verbose_name = 'Video content'
        verbose_name_plural = 'Video content'

    def __str__(self):
        return self.title


class AboutUs(TimestampedModel):
    content = models.TextField()
    image = models.ImageField(upload_to='about/')
    headline = models.CharField(max_length=180, default='Built on trust, precision, and craftsmanship.')

    class Meta:
        verbose_name = 'About us'
        verbose_name_plural = 'About us'

    def __str__(self):
        return self.headline


class ContactInfo(TimestampedModel):
    phone = models.CharField(max_length=40)
    email = models.EmailField()
    address = models.TextField()
    map_embed = models.TextField(help_text='Paste the Google Maps iframe embed code.')
    business_hours = models.CharField(max_length=120, blank=True)

    class Meta:
        verbose_name = 'Contact information'
        verbose_name_plural = 'Contact information'

    def __str__(self):
        return self.email


class SocialMedia(TimestampedModel):
    platform_name = models.CharField(max_length=80)
    icon_class = models.CharField(max_length=80, help_text='Font Awesome or Bootstrap Icons class.')
    url = models.URLField()
    display_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['display_order', 'platform_name']
        verbose_name = 'Social media link'
        verbose_name_plural = 'Social media links'

    def __str__(self):
        return self.platform_name
