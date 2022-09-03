from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('order/', views.ordering_form, name='ordering_form'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
