import os 
from sys import argv


ListeFichier = list()
ListeDossier = list()


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

print(ListeDossier)
print(ListeFichier)