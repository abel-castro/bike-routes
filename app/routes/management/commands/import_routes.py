import json

from django.core.management.base import BaseCommand
from django.utils import timezone

from routes.models import Route


class Command(BaseCommand):
    help = "Import routes from a JSON file"

    @staticmethod
    def _create_route_name() -> str:
        return f"Route imported at {timezone.now()}"

    def add_arguments(self, parser):
        parser.add_argument("file_path", type=str)

    def handle(self, *args, **options):
        file_path = options["file_path"]
        with open(file_path) as json_file:
            routes = json.load(json_file)
            json_file.close()

        imported_routes = 0
        for data in routes:
            route, created = Route.objects.get_or_create(
                data=data, defaults={"name": self._create_route_name()}
            )

            if created:
                imported_routes += 1

        print(f"{imported_routes} routes were imported")
