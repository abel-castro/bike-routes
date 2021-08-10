from django.core.management import call_command
from pytest import mark

from routes.models import Route


@mark.django_db
def test_import_routes():
    call_command("import_routes", file_path="routes/tests/test_data.json")

    routes = Route.objects.all()
    assert routes.count() == 2
