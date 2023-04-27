
from voitures import voitures # importer du fichier voitures la class voiture 
from bus import bus
from moto import moto


### test de la class voitures
voiture1 = voitures("bmw","M5","black",4,2000)
voiture2 = voitures("seat","leon","grise",4,2019)
voiture1.get_informations()
voiture1.set_newannee(2009)

### test de la class bus

bus1 = bus("volvo","M5","blanc",8,2000)
bus2 = bus("renault","R312","gris",8,1980)
bus1.get_informations()
bus2.get_informations()

### test de la class moto

moto1 = moto("Kawasaki","Z800","noir",2,2000)
moto2 = moto("Yamaha","Z1000","bleu",2,2010)
moto1.get_informations()
moto2.get_informations()


def get_couleur_car (self):

    if (self.couleur == "rouge"):
        print(f"{voitures.get_informations()}")
    else :
        print(f"ya pas de voiture avec une couleur {get_couleur_car()}")



