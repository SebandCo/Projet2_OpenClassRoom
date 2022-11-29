from projet2_masson_fonction import *
from tqdm import tqdm #Permet d'afficher une barrde de progression
import time #Pour voir combien de temps dure un programme

#------- Début du chrono
start_time = time.time()    

#------- Adresse du site à analyser
url_general="https://books.toscrape.com"

#------- Définir l'ordre des colonnes CSV
liste_entete=[
    "title",
    "category",
    "image",
    "url",
    "upc",
    "tax",
    "no_tax",
    "availability",
    "description", 
    "review",
    ]
#------- Définir la valeur des entêtes CSV
dico_entete={
    "url"          : "Product_page_url",
    "upc"          : "Universal_product_code (upc)",
    "title"        : "Title",
    "tax"          : "Price_including_tax",
    "no_tax"       : "Price_excluding_tax",
    "availability" : "Number_available",
    "description"  : "Product_description",
    "category"     : "Category",   
    "review"       : "Review_rating",
    "image"        : "Image_url"
    }
#------ Définir le nom du fichier csv
nom_du_csv="export_livre"
#------ Définir le nom du fichier csv image
fichier_image="image"

#------ Initialisation du fichier csv
creation_csv(liste_entete, dico_entete,nom_du_csv)


#------ lancement de la fonction pour exporter les catégories
dico_categorie={}# Création d'un dico vide pour les URL des categories
lancement_export_categorie(url_general,dico_categorie)#Lance le programme

nbr=1#compteur du nombre de catégorie

for key_categorie in dico_categorie:
    liste_ouvrage_categorie=[] #Création d'un liste vide pour les ouvrages    
    url_actuel_categorie=dico_categorie[key_categorie] #Défini l'URL de la catégorie en cours
    
#------ Export des livres par catégorie
    lancement_export_ouvrage(url_general,url_actuel_categorie, liste_ouvrage_categorie)#lancement du programme
    
    print ("Analyse des",len(liste_ouvrage_categorie),"livres de la catégorie", key_categorie,"(Categorie",nbr,"/",len(dico_categorie),")")
    nbr+=1#incrémente l'avancée des categories
#------ Lancement de la boucle pour chaque livre de la catégorie en cours avec barre de progression
    for livre in tqdm(liste_ouvrage_categorie,desc="Analyse en cours", unit="livre"):
        url_courant_livre=livre #Défini le livre en cours
        analyse_livre(liste_entete,dico_entete,url_general,url_courant_livre,nom_du_csv,fichier_image) #Lance le programme

print("Fin de l'analyse","\nAnalyse réalisée en",int(time.time() - start_time),"secondes")#Fin du programme