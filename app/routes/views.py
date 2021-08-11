from django.views.generic import TemplateView
from rest_framework import viewsets

from routes.models import Route
from routes.serializers import RouteSerializer


class HomeView(TemplateView):
    template_name = "home.html"


class RoutesViewSet(viewsets.ModelViewSet):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer
