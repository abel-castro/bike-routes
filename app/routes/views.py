from django.conf import settings
from django.views.generic import DetailView, TemplateView
from rest_framework import viewsets

from routes.models import Route
from routes.serializers import RouteSerializer


class HomeView(TemplateView):
    template_name = "home.html"


class RoutesViewSet(viewsets.ModelViewSet):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer


class RouteDetailView(DetailView):
    model = Route
    template_name = "route_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['MAPTILER_API_KEY'] = settings.MAPTILER_API_KEY
        return context
