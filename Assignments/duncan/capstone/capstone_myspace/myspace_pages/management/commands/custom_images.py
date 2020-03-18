import os
from pathlib import Path
from django.core.management.base import BaseCommand, CommandError
from myspace_pages.models import ProfilePicChoice, ProfileMusicChoice

other_folder = 'media'

# media_dir_file = os.path.abspath(__file__)
# media_dir = os.path.dirname(media_dir_file)
# base_dir = os.path.dirname(media_dir)

class Command(BaseCommand):

    def handle(self, *args, **options):
        base_dir = os.path.dirname(
            os.path.dirname(
                os.path.dirname(
                    os.path.dirname(
                        os.path.abspath(__file__)
                    )
                )
            )
        )
        # print(base_dir)

        media_dir = os.path.join(base_dir, 'media')
        # print(media_dir)

        other_dir = os.path.join(
            os.path.dirname(
                os.path.dirname(
                    os.path.dirname(
                        os.path.dirname(
                            os.path.abspath(__file__)
                        )
                    )
                )
            ), 'media', 'profile_pics')
        # print(other_dir)

        music_dir = os.path.join(
            os.path.dirname(
                os.path.dirname(
                    os.path.dirname(
                        os.path.dirname(
                            os.path.abspath(__file__)
                        )
                    )
                )
            ), 'media', 'music')

        for one_file in Path(other_dir).glob('*'):
            if str(one_file)[-3:] in ['png', 'jpg']:
                print(one_file.relative_to(media_dir))
                ProfilePicChoice.objects.get_or_create(image=str(one_file.relative_to(media_dir))) #relative_to ??
        
        for one_file in Path(music_dir).glob('*'):
            if str(one_file)[-3:] == 'mp3':
                print(one_file.relative_to(media_dir))
                ProfileMusicChoice.objects.get_or_create(music=str(one_file.relative_to(media_dir))) 