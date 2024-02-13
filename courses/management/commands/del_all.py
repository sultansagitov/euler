from django.core.management.base import BaseCommand
from courses.models import CourseType


class Command(BaseCommand):
    help = "Deletes all courses (with all course types)"

    def handle(self, *args, **options):
        for item in CourseType.objects.all():
            item.delete()