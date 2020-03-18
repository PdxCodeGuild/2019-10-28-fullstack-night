import os
from pathlib import Path

other_folder = 'media'
media_dir_file = os.path.abspath(__file__)
print(media_dir_file)

media_dir = os.path.dirname(media_dir_file)
print(media_dir)

base_dir = os.path.dirname(media_dir)
print(base_dir)

other_dir = os.path.join(base_dir, 'media')
print(other_dir)

for one_file in Path(other_dir).glob('*'):
    print(one_file)