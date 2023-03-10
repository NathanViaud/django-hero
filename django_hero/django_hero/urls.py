from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('book/', include('book.urls')),
    path('authentification/', include('authentification.urls')),
    path('', RedirectView.as_view(url='authentification/login'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
