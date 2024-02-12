import os
from sys import argv




def affiche():
    for i in os.listdir(argv[1]):
        print(i)

def main() :
        try:
            if len(argv) == 1:
                print("Aucun argument n'a été passé en paramètre")
            
            elif os.path.exists(argv[1]) == False:
                print("Le dossier n'existe pas")
            else:
                 affiche()    
        except Exception as e:
            print("[?] Une erreur est survenue: [?]", e)

if __name__ == "__main__":
    main()



# os.chdir(d) : permet d’aller dans le dossier d correspondant
# • os.listdir(d) : permet d’obtenir une liste de fichiers et dossiers contenu dans le
# dossier d.
# • os.environ[nom_variable] : liste des variables d’environnement que vous
# pouvez consulter en tapant dans une fenêtre cmd la commande set
# o Par exemple, dans un script python, avec os.environ["USSERNAME"],
# vous obtenez votre nom d’utilisateur (eXXXXXXX).
# • os.path.exists(d) : permet de vérifier l’existence du dossier d