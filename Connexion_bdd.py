import mysql.connector as mysqlpyth
from Apprenants import Apprenants

class Connexion :

#Connexion à la base de donnée

    def __init__(self) :
        
        self.connexion = mysqlpyth.connect(
            host="localhost",
            port="3306",
            user="root", 
            password="root", 
            database="binomotron")
        self.cursor = self.connexion.cursor()

# Fonction permettant de  créer la  colonne mail dans la table apprenant 
    
    def creation_colonne_mail (self):

        self.cursor.execute("ALTER TABLE apprenant ADD COLUMN IF NOT EXISTS mail  VARCHAR(100) NOT NULL;")
    
        self.cursor.close()
        self.connexion.close()

 # Fonction permettant de récupérer les infos dans la table apprenant et de les afficher plus tard via la classe Apprenants

    def recup_info (self):
            
            groupe = []
            
            self.cursor.execute("SELECT nom, prenom, id_apprenant,mail FROM apprenant")
            
            for nom, prenom, id_apprenant,mail in self.cursor :
                nouveau = Apprenants(nom, prenom,id_apprenant, mail)
                groupe.append(nouveau)
            
            self.cursor.close()
            self.connexion.close()
            return groupe

 # Fonction permettant de récuperer les noms des apprenants dans la base de données

    def recup_nom (self):
            
            self.nomlower = []
    
            self.cursor.execute("SELECT nom FROM apprenant")
            self.nom = [i[0] for i in self.cursor.fetchall()]
            #print(self.nom)
            
            for i in self.nom:
                
                i = i.lower()
                i = i.replace(" ","")
                i = i.replace("'","")
                self.nomlower.append(i)

            self.cursor.close()
            self.connexion.close()
            return self.nomlower

# Fonction permettant de récuperer les id des apprenants dans la base de données

    def recup_id_apprenant (self):

        self.cursor.execute ("SELECT id_apprenant FROM apprenant")
        self.id_apprenant = [i[0] for i in self.cursor.fetchall()]
        self.cursor.close()
        self.connexion.close()
        return self.id_apprenant

# Fonction permettant de récuperer d'insérer les mails récupérés dans un fichier.doc externe et de les insérer par la suite dans la bdd 

    def insertion (self,mail,id_apprenant):

        self.cursor.execute("UPDATE apprenant SET mail = '%s' WHERE id_apprenant = '%s'"%(mail, id_apprenant))
        self.connexion.commit()
        self.cursor.close()
        self.connexion.close()


        

