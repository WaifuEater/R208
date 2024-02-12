import os
from sys import argv

ListeFichier = list()
ListeDossier = list()


if len(argv) == 1:
    arg = argv[1]

def recherche(arg):
     for i in os.listdir(argv[1]):
        if os.path.isfile(i):
            ListeFichier.append(i)
        elif os.path.isdir(i):
            ListeDossier.append(i)
            for j in os.listdir(i):
                if os.path.isfile(j):
                    ListeFichier.append(j)
                elif os.path.isdir(j):
                    ListeDossier.append(j)    
  
def main():
    try:
        if len(argv) == 1:
            print("Aucun argument n'a été passé en paramètre")
        
        elif os.path.exists(argv[1]) == False:
            print("Le dossier n'existe pas")
        else:
            recherche(argv[1])
            print("Liste des fichiers:")
            for i in ListeFichier:
                print(i)
            print("Liste des dossiers:")
            for i in ListeDossier:
                print(i)
            
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