from . import views
from django.urls import path

urlpatterns = [
    path('',views.homepage,name='homepage'),
    path('list/',views.event_list,name='list'),
    path('details/',views.details,name='details')
]