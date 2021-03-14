from django.urls import path
from django.conf import settings
from .views import login_redirect
from django.conf.urls.static import static

urlpatterns = [
    path('', login_redirect),
] + static(settings.UPLOAD_FILES['URL'], document_root=settings.UPLOAD_FILES['ROOT'])
