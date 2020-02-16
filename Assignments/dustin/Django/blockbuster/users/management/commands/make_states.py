from django.core.management.base import BaseCommand, CommandError
from users.models import State
from movies.models import Condition, Genre

class Command(BaseCommand):
    def handle(self, *args, **options):
        initials = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY', 'AS', 'DC', 'FM', 'GU', 'MH', 'MP', 'PW', 'PR', 'VI']

        for initial in initials:
            # State(text=initial).save()
            State.objects.get_or_create(text=initial)

        condition_list = ['GREAT', 'GOOD', 'FAIR', 'POOR', 'EVIL']
        for condition in condition_list:
            Condition.objects.get_or_create(text=condition)
            
        genre_list = ['Action', 'Adult', 'Adventure', 'Animation / Anime', 'Biopic', 'Childrens', 'Comedy', 'Crime / detective /spy', 'Documentary', 'Drama', 'Horror', 'Family', 'Fantasy', 'Historical', 'Medical', 'Musical', 'Paranormal', 'Romance', 'Sport', 'Science fiction', 'Talk Show', 'Thriller / Suspense', 'War', 'Western']

        for genre in genre_list:
            Genre.objects.get_or_create(text=genre)

