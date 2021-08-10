import factory

from routes.models import Route


class RouteFactory(factory.django.DjangoModelFactory):
    name = factory.Sequence(lambda n: "Box %d" % n)
    data = {"polyline": [[[16.354, 48.27571]]], "pois": []}

    class Meta:
        model = Route
        django_get_or_create = ("name",)
