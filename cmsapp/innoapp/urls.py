from django.urls import path

from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('list/', views.event_list, name='list'),
    path('details/', views.event_detail, name='details'),
    path('details/<slug:slug>/', views.event_detail, name='details_by_slug'),
]
