from django.core.management import call_command
from pytest import mark

from routes.models import Route


@mark.django_db
def test_import_routes():
    call_command("import_routes", "routes/tests/test_data.json")

    assert Route.objects.count() == 2

    call_command("import_routes", "routes/tests/test_data.json")

    assert Route.objects.count() == 2
