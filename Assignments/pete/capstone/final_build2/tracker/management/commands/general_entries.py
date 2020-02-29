from django.core.management.base import BaseCommand, CommandError

from tracker.models import Meal

import json

def get_meals(meals_json):
    with open(meals_json) as f:
        return json.loads(f.read())

class Command(BaseCommand):
    def handle(self, *args, **options):
        with open('tracker/management/commands/general_entries.json') as f:
            meals = json.loads(f.read())
        
        for meal in meals:
            Meal.objects.get_or_create(
                name = meal['name'],
                kcal = meal['kcal'],
                fat = meal['fat'],
                carb = meal['carb'],
                protein = meal['protein'],
                general = True,
            )