from django.core.management import call_command
from pytest import mark

from routes.models import Route


@mark.django_db
def test_import_routes__no_duplicates():
    """
    Verify that the importer data is correct and that objects
    """
    call_command("import_routes", "routes/tests/test_data/multiple_routes.json")

    assert Route.objects.count() == 2

    call_command("import_routes", "routes/tests/test_data/multiple_routes.json")

    assert Route.objects.count() == 2


@mark.django_db
def test_import_routes__values():
    expected_data = [[16.354, 48.27571], [16.35444, 48.27522]]
    call_command("import_routes", "routes/tests/test_data/single_route.json")
    route = Route.objects.get()

    assert route.data == expected_data


@mark.django_db
def test_import_routes__wrong_data():
    call_command("import_routes", "routes/tests/test_data/single_route_wrong_data.json")
    assert Route.objects.count() == 0
