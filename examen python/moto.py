class moto:
    def __init__ (self,marque,model,couleur,nb_roues,annee):
          self.marque = marque
          self.model = model
          self.couleur = couleur
          self.annee = annee
          self.nb_roues = nb_roues
          

    def get_informations (self):
        if ( self.nb_roues == 2 ):
            print(f" la moto est de marque {self.marque} le model est {self.model} est de couleur {self.couleur} l'annee de fabrication {self.annee} nombre de roues est : {self.nb_roues} roues ")
        else :
           print(f"vous vous trompez sur le nombre de roues ...") 


    def get_annee(self):
        print(f"l annee de fabrication de la moto est de : {self.annee}")






moto1 = moto("Kawasaki","Z800","noir",2,2000)
moto2 = moto("Yamaha","Z1000","bleu",2,2010)
moto1.get_informations()
moto2.get_informations()
moto1.get_annee()
moto3 = moto("Kawasaki","Z800","noir",3,2000)
moto4 = moto("Yamaha","Z1000","bleu",1,2010)
moto3.get_informations()



