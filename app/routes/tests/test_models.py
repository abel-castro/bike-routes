from pytest import mark

from routes.models import Route
from routes.tests.factories import RouteFactory


@mark.django_db
def test__route__random_sample_image():
    route = RouteFactory.create()

    assert route.image in Route.SAMPLE_IMAGES
