from django.urls import path
from django.conf.urls.static import static
from . import views
from django.conf import settings

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('list/', views.event_list, name='list'),
    path('details/', views.event_detail, name='details'),
    path('details/<slug:slug>/', views.event_detail, name='details_by_slug'),
    path("login/", views.member_login, name="member_login"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)