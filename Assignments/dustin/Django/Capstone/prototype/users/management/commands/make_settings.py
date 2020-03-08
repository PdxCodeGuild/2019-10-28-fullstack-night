from django.core.management.base import BaseCommand, CommandError
from users.models import Theme, Layout, Medium


class Command(BaseCommand):
    def handle(self, *args, **options):
        themes = ['Dark', 'Light']
        for theme in themes:
            # State(text=initial).save()
            Theme.objects.get_or_create(text=theme)

        layouts = ['Type 1', 'Type 2', 'Type 3']
        for layout in layouts:
            Layout.objects.get_or_create(text=layout)
            
        mediums = ['Pen/Pencil', 'Paints', 'Digital Illustrations', 'Digital Manipulation', 'Photography', 'Poetry', 'Short Stories', 'Novels', 'Music', 'Broadcast', 'Videography']
        for medium in mediums:
            Medium.objects.get_or_create(text=medium)
