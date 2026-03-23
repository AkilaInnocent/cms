from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('content', models.TextField()),
                ('image', models.ImageField(upload_to='about/')),
                ('headline', models.CharField(default='Built on trust, precision, and craftsmanship.', max_length=180)),
            ],
            options={'verbose_name': 'About us', 'verbose_name_plural': 'About us'},
        ),
        migrations.CreateModel(
            name='ContactInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('phone', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.TextField()),
                ('map_embed', models.TextField(help_text='Paste the Google Maps iframe embed code.')),
                ('business_hours', models.CharField(blank=True, max_length=120)),
            ],
            options={'verbose_name': 'Contact information', 'verbose_name_plural': 'Contact information'},
        ),
        migrations.CreateModel(
            name='HeroSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=200)),
                ('subtitle', models.TextField()),
                ('background_image', models.ImageField(upload_to='hero/')),
                ('call_to_action_text', models.CharField(max_length=80)),
                ('call_to_action_link', models.CharField(help_text='Use an internal anchor like #contact or a full URL.', max_length=200)),
            ],
            options={'verbose_name': 'Hero section', 'verbose_name_plural': 'Hero sections'},
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='projects/')),
                ('video_url', models.URLField(blank=True)),
                ('category', models.CharField(choices=[('construction', 'Construction'), ('masonry', 'Masonry'), ('craftsmanship', 'Craftsmanship'), ('home-crafts', 'Home Crafts'), ('water-repair', 'Water Repair'), ('plumbing', 'Plumbing Construction')], max_length=40)),
                ('slug', models.SlugField(blank=True, max_length=170, unique=True)),
                ('featured', models.BooleanField(default=False)),
            ],
            options={'ordering': ['-featured', '-created_at']},
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('icon', models.CharField(blank=True, help_text='Optional Bootstrap Icons class, e.g. bi bi-hammer.', max_length=80)),
                ('image', models.ImageField(upload_to='services/')),
                ('display_order', models.PositiveIntegerField(default=0)),
            ],
            options={'ordering': ['display_order', 'title']},
        ),
        migrations.CreateModel(
            name='SocialMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('platform_name', models.CharField(max_length=80)),
                ('icon_class', models.CharField(help_text='Font Awesome or Bootstrap Icons class.', max_length=80)),
                ('url', models.URLField()),
                ('display_order', models.PositiveIntegerField(default=0)),
            ],
            options={'verbose_name': 'Social media link', 'verbose_name_plural': 'Social media links', 'ordering': ['display_order', 'platform_name']},
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=120)),
                ('message', models.TextField()),
                ('rating', models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])),
                ('image', models.ImageField(blank=True, upload_to='testimonials/')),
            ],
            options={'ordering': ['-created_at']},
        ),
        migrations.CreateModel(
            name='VideoContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=150)),
                ('video_url', models.URLField()),
                ('thumbnail', models.ImageField(upload_to='videos/thumbnails/')),
                ('display_order', models.PositiveIntegerField(default=0)),
            ],
            options={'verbose_name': 'Video content', 'verbose_name_plural': 'Video content', 'ordering': ['display_order', 'title']},
        ),
    ]
