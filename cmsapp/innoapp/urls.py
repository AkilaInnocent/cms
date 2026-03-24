from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('list/', views.event_list, name='list'),
    path('details/', views.event_detail, name='details'),
    path('details/<slug:slug>/', views.event_detail, name='details_by_slug'),
    path('contact-submit/', views.contact_submit, name='contact_submit'),
    path('newsletter-subscribe/', views.newsletter_subscribe, name='newsletter_subscribe'),
    path('login/', views.member_login, name='member_login'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
