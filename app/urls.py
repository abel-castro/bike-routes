"""bike_routes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from routes.views import HomeView, RouteDetailView, RoutesViewSet

router = DefaultRouter()
router.register(r"routes", RoutesViewSet, basename="routes")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path(r"", HomeView.as_view(), name="home"),
    path(r"routes/<pk>/", RouteDetailView.as_view(), name="detail"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
