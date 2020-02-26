from django.core.management.base import BaseCommand, CommandError
from autocomplete.models import Animal

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'


    def handle(self, *args, **options):
        for animal in ['Lion', 'Squirrel', 'SnowLeopard', 'DogGoldendoodle', 'RedPanda', 'Raccoon', 'RedPanda', 'Tiger', 'RedPanda', 'MonkeySquirrelMonkey', 'Wolf', 'TigerMalayanTiger', 'Lion', 'DogGoldendoodle', 'Dog', 'RedPanda', 'Kitten', 'WolfGrayWolf', 'WolfGrayWolf', 'EagleBaldEagle', 'MacawScarletMacaw', 'HeronGreatBlueHeron', 'OwlBarredOwl', 'ButterflyPipevineSwallowtail', 'PolarBear', 'MoorhenCommonGallinule', 'Kookaburra', 'GoldenHamster', 'BirdLimpkin', 'PuppyChug', 'GuineaPig', 'RedPanda', 'GiantTortoiseAldabraGiantTortoise', 'BeardedDragonCentralBeardedDragon', 'Alligator', 'Tiger', 'StorkSaddlebilledStork', 'Owl', 'PrairieDog', 'Hamster', 'WolfGrayWolf', 'EgretGreatEgret', 'PuppyGoldendoodlePuppy', 'Egret', 'TigerSiberianTiger', 'SeaLionCaliforniaSeaLion', 'Rabbit', 'Puppy', 'TurtleBlackSoftshellTurtle', 'RedPanda', 'IbisScarletIbis', 'FinchAmericanGoldfinch', 'DogBorderCollie', 'TigerMalayanTiger', 'Tiger', 'RedPanda', 'PantherFloridaPanther', 'OwlGreatHornedOwl', 'Wolf', 'OwlBarredOwl', 'Rabbit', 'BirdPaintedBunting', 'ButterflyZebraLongwing', 'PenguinAfricanPenguin', 'MacawScarletMacaw', 'DinosaurSpinosaurus', 'DogSchipperke', 'ButterflyLongwing', 'SnowLeopard', 'RedPanda', 'Cougar', 'Peafowl', 'EgretSnowyEgret', 'Puppy', 'PantherFloridaPanther', 'WolfGrayWolf', 'WolfGrayWolf', 'Meerkat', 'Peafowl', 'BirdSunbittern', 'GuineaPig', 'EgretSnowyEgret', 'AsianBlackBear', 'Raccoon', 'Lion', 'ElephantAfricanElephant', 'DogChihuahua', 'Raccoon', 'GiantTortoiseAldabraGiantTortoise', 'StarlingEmeraldStarling', 'Lion', 'Ibis', 'HamsterGoldenHamster', 'GiantTortoise', 'EgretSnowyEgret', 'Hornet', 'SnowLeopard', 'LeopardAmurLeopard', 'Falcon']:
            Animal.objects.get_or_create(name=animal)
