from typing import Any
from bharu.models import category
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "this commands inserts category data"

    def handle(self, *args: Any, **options: Any):
           #delete existing data 
           category.objects.all().delete()
           categories = ['sports','technology','scince','art','foood']
           for category_name in categories:
                category.objects.create(name= category_name)

           self.stdout.write(self.style.SUCCESS("Completed inserting data"))    