from os import fdopen
from Connexion_bdd import Connexion
from Apprenants import Apprenants
from Class_fichier import Fichier


def main():
       
   tous = Connexion().recup_info()

   for Apprenants in tous :
       
       print(Apprenants.nom, Apprenants.prenom, Apprenants.mail)
'''
Insertion des mails dans la bdd
'''
Fichier(fdopen).traitement()
'''
Création de la colonne mail dans la table apprenant 
'''
#Connexion().creation_colonne_mail()

'''
Affichage des données que l'on désire dans la base de données
'''
main()