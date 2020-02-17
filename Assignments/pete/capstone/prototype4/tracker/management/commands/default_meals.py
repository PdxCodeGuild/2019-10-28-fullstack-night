from django.core.management.base import BaseCommand, CommandError

from tracker.models import Meal

import json

def get_meals(meals_json):
    with open(meals_json) as f:
        return json.loads(f.read())

class Command(BaseCommand):

    # def add_arguments(self, parser):
    #     parser.add_argument('--add', type=str, help="Args: <name> <kcal> <fat> <carb> <protein>")

    #     parser.add_argument('integers', nargs=4)

    #     # args = parser.parse_args()


    def handle(self, *args, **options):
        # add = options['add']
        # integers = options['integers']
        with open('tracker/management/commands/default_meals.json') as f:
            meals = json.loads(f.read())
        
        # headers = ['name', 'kcal', 'fat', 'carb', 'protein']
        for meal in meals:
            Meal.objects.get_or_create(
                name = meal['name'],
                kcal = meal['kcal'],
                fat = meal['fat'],
                carb = meal['carb'],
                protein = meal['protein'],
                general = True,
            )
            # print(meal)

        # if options['add']:
        #     Meal.objects.get_or_create(
        #         name = add,
        #         kcal = integers[0],
        #         fat = integers[1],
        #         carb = integers[2],
        #         protein = integers[3],
        #         general = True,
        #     )

        for meal in Meal.objects.filter(general=True):
            print(meal)
        
        print(args)
        # print(add)
        # print(integers)