from os import fdopen
from Connexion_bdd import Connexion


class Fichier:


    def __init__(self,fichier):

        self.fichier = fichier

#Lecture du fichier

    def recup_fichier (self) :
        
        liste  = []
        self.fichier = open("C:/Users/Sialorama/Google Drive/STEPHANE/SEMAINE 10/Mails Apprenants/apprenantmail.txt", "r")
        
        for ligne in self.fichier :
            
            liste.append(ligne.strip())
            
        
        self.fichier.close()
        return liste 
    
# Fonction permettant de creer un dictionnaire ayant pour clé les noms des apprenants et en valeur le mail de celui-ci
 
    def dico_nom_mail (self):
        
        self.nom_traiter = []
        self.nom_bdd = Connexion().recup_nom()
        self.fichier_mail = Fichier(fdopen).recup_fichier()
        
        for mail in self.fichier_mail:
           
            self.nom_fichier = mail.split("@")[0].split(".")[1]
            self.nom_fichier = self.nom_fichier.replace("-","")
            self.nom_traiter.append(self.nom_fichier)
        
        dico_nom_mail = {x:y for x, y in zip(self.nom_traiter,self.fichier_mail)}
        #print (dico_nom_mail)
        return dico_nom_mail

# Fonction permettant de creer un dictionnaire ayant pour clé les noms des apprenants et en valeur l'id celui-ci dans la base de donnée

    def dico_nom_id_apprenants (self):
            
        self.id_apprenant = Connexion().recup_id_apprenant()
        self.nom_bdd = Connexion().recup_nom()
        dico_nom_id_apprenant = {x:y for x, y in zip(self.nom_bdd,self.id_apprenant)}

        print (dico_nom_id_apprenant)
        return dico_nom_id_apprenant
           

# Fonction permettant de verifier que deux dictionnaires on la même clé si c'est le cas elle récupère les valeurs qu'a cette clé dans les 2 dictionnaires 
# Ensuite elle insère la valeur du premier dictionnaire à savoir le mail où la deuxième valeur à savoir l'id de l'apprenant se trouve dans la base de donnée
    
    def traitement (self):

        self.dico_nom_id_apprenants = Fichier(fdopen).dico_nom_id_apprenants()
        self.dico_nom_mail = Fichier(fdopen).dico_nom_mail()
        #print (self.dico_nom_mail)
        #print (self.dico_nom_id_apprenants)
        
        for cle in self.dico_nom_id_apprenants.keys():
            if  cle in self.dico_nom_mail.keys():
                 
                 self.mail = self.dico_nom_mail[cle]
                 self.id_apprenant = self.dico_nom_id_apprenants[cle]
                 #print (self.mail,'\n',self.id_apprenant)
                 Connexion().insertion(self.mail,self.id_apprenant)

