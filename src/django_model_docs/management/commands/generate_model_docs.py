from django.core.management.base import BaseCommand
from django_model_docs.serializers.app_serializer import (
    AppSerializer,
)


class Command(BaseCommand):
    app_serializer = AppSerializer()

    """
    Generate markdown file from a given django app name
    """

    def add_arguments(self, parser):
        parser.add_argument("app", type=str, help="Django app module name")
        parser.add_argument(
            "-o",
            "--out-file",
            type=str,
            required=True,
            help="Name of markdown file to create",
        )

    def handle(self, *args, **options):
        """
        Generate docs/data_dictionary.md file.
        """

        app_name = options["app"]
        out_file = options["out_file"]

        data_dictionary = self.app_serializer.markdown(app_name)

        with open(out_file, "w") as fh:
            fh.write(data_dictionary)

        print(f"\nGenerated file: {out_file}")
