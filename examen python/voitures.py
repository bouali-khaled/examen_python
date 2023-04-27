class voitures:
    def __init__ (self,marque,model,couleur,nb_roues,annee):
          self.marque = marque
          self.model = model
          self.couleur = couleur
          self.annee = annee
          self.nb_roues = nb_roues
          

    def get_informations (self):
        print(f" la voiture est de marque {self.marque} le model est {self.model} de couleur {self.couleur} l'annee de fabrication {self.annee} nombre de roues est : {self.nb_roues} roues ")

    def get_nb_roues (self):
        if (self.nb_roues < 4):
         print(f"le nombres de roues saisi est incoherant avec le nombre de roues d'une voiture ")
        else :
         print(f"le nombre de roues est de : {self.nb_roues} roues ")

    def set_newannee (self, newannee):
         self.newannee = newannee
         print(f"la nouvelle annee  de la voiture est :{self.newannee}")

    

    


  


voiture1 = voitures("bmw","M5","black",4,2000)
voiture2 = voitures("seat","leon","grise",4,2019)
voiture1.get_informations()
voiture2.get_informations()
voiture1.set_newannee(2009)
voiture2.set_newannee(2006) 
voiture3 = voitures("seat","leon","grise",2,2019)
voiture3.get_nb_roues()

