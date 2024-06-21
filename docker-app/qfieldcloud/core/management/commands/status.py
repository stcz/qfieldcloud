from django.core.management.base import BaseCommand
from qfieldcloud.core import geodb_utils, utils


class Command(BaseCommand):
    help = "Check qfieldcloud status"

    def handle(self, *args, **options):
        results = {}

        results["geodb"] = "ok"
        # Check geodb
        if not geodb_utils.geodb_is_running():
            results["geodb"] = "error"

        results["storage"] = "ok"
        # Check if bucket exists (i.e. the connection works)
        try:
            utils.get_s3_bucket()
        except Exception:
            results["storage"] = "error"

        self.stdout.write(
            self.style.SUCCESS(f"Everything seems to work properly: {results}")
        )
