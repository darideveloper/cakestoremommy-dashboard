
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from django.urls import include

from rest_framework import routers

from content import views as content_views


# Setup drf router
router = routers.DefaultRouter()
router.register(
    r'gallery-images',
    content_views.GalleryImageViewSet,
    basename='gallery-images'
)
router.register(
    r'categories',
    content_views.CategoryViewSet,
    basename='categories'
)

urlpatterns = [
    # Admin site
    path('admin/', admin.site.urls),
    
    # Redirects
    path(
        '',
        RedirectView.as_view(url='/admin/'),
        name='home-redirect-admin'
    ),
    path(
        'accounts/login/',
        RedirectView.as_view(url='/admin/'),
        name='login-redirect-admin'
    ),
    
    # API URLs
    path('api/', include(router.urls)),
    
]


if not settings.STORAGE_AWS:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)