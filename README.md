# Projet2_OpenClassRoom
Projet 2 : Scrapping d'un site Web (https://books.toscrape.com/)

##### L'objectif :
- Extraire les informations de l'ensemble de la bibliotheque du site

##### Le resultat :
- Un fichier .csv transposable en .xls de l'ensemble des données des livres du site
- Un dossier comprenant l'ensemble des images de couverture des infos-livres extraits

##### Le programme :
Il est composé de :
- Deux fichiers python. L'un contenant l'ensemble des fonctions et l'autre permettant le lancement des fonctions
- Un fichier requirements.txt pour la mise en place de l'environnement virtuel

##### Deux solutions distincts :
- Une première suivant le déroulé logique de l'exercice à savoir :
(*projet2_masson_fonction.py* et *projet2_masson_lancement.py*)
  - 1er étape    : Extraction des catégories
  - 2eme étape   : Extraction de la liste par catégorie
  - 3eme étape   : Extraction des infos livres par catégorie
  - Avantages    : Solution modulable qui permet une évolution vers une recherche par catégorie ou ouvrage
  - Inconvenient : Programme assez long (25/30 min)
  
- Une deuxième avec un objectif plus tournée vers la veille régulière :
(*projet2_masson_fonction_v2.py* et *projet2_masson_lancement_v2.py*)
  - 1er étape    : Extraction de l'ensemble des livres
  - 2eme étape   : Extraction des infos livres en masse
  - Avantage     : Programme plus rapide (15min environ). Gagne en rapidité quand l'image du livre existe déjà dans le repertoire
  - Inconvenient : Modularité plus compliquée à mettre en place

