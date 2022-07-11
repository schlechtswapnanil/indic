from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.base, name='blog'),
    path('home/', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)