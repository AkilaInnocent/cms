from urllib.parse import parse_qs, urlparse

from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter
def render_map(value):
    return mark_safe(value or '')


@register.filter
def embed_video(url):
    if not url:
        return ''
    parsed = urlparse(url)
    host = parsed.netloc.lower()

    if 'youtube.com' in host:
        video_id = parse_qs(parsed.query).get('v', [''])[0]
        return f'https://www.youtube.com/embed/{video_id}' if video_id else url
    if 'youtu.be' in host:
        video_id = parsed.path.strip('/')
        return f'https://www.youtube.com/embed/{video_id}' if video_id else url
    if 'vimeo.com' in host:
        video_id = parsed.path.strip('/').split('/')[-1]
        return f'https://player.vimeo.com/video/{video_id}' if video_id else url
    return url


@register.filter
def star_range(value):
    try:
        return range(int(value))
    except (TypeError, ValueError):
        return range(0)


@register.filter
def slugify_css(value):
    return str(value).replace(' ', '-').replace('_', '-').lower()
