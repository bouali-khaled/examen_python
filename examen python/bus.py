class bus:
    def __init__ (self,marque,model,couleur,nb_roues,annee):
          self.marque = marque
          self.model = model
          self.couleur = couleur
          self.annee = annee
          self.nb_roues = nb_roues
          

    def get_informations (self):
        print(f" le bus est de marque {self.marque} le model est {self.model}  est de couleur{self.couleur} l'annee de fabrication {self.annee} nombre de roues est : {self.nb_roues} roues ")


    def get_nb_roues (self):
        if (self.nb_roues < 8):
         print(f"le nombres de roues saisi est incoherant avec le nombre de roues d'un bus ({self.nb_roues}) qui est de 8 roues ")
        else :
         print(f"le nombre de roues est de : {self.nb_roues} roues ")

    def set_newannee (self, newannee):
         self.newannee = newannee
         print(f"la nouvelle annee  de la voiture est :{self.newannee}")
  


bus1 = bus("volvo","M5","blanc",8,2000)
bus2 = bus("renault","R312","gris",8,1980)
bus1.get_informations()
bus2.get_informations()
bus3 = bus("volvo","M5","blanc",7,2000)
bus3.get_nb_roues()
bus3.set_newannee(200000)
