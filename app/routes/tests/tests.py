from django.shortcuts import resolve_url
from pytest import mark
from rest_framework import status

from routes.models import Route
from routes.tests.factories import RouteFactory


URL = "/api/routes/"


@mark.django_db
def test_create(client):
    expected_name = "My new route"
    expected_data = {"test": "data"}
    data = {"name": expected_name, "data": expected_data}
    response = client.post(URL, data, content_type="application/json")
    assert response.status_code == status.HTTP_201_CREATED
    new_route = Route.objects.get()
    assert new_route.name == expected_name
    assert new_route.data == expected_data


@mark.django_db
def test_list(client):
    RouteFactory.create_batch(5)
    response = client.get(URL)

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 5


@mark.django_db
def test_get(client):
    route = RouteFactory.create()
    url = f"{URL}{route.id}"
    response = client.get(url, follow=True)

    assert response.status_code == status.HTTP_200_OK
    assert response.data["id"] == route.id
    assert response.data["name"] == route.name
    assert response.data["data"] == route.data


@mark.django_db
def test_delete(client):
    route = RouteFactory.create()
    url = f"{URL}{route.id}"
    response = client.delete(url, follow=True)

    assert response.status_code == status.HTTP_200_OK
