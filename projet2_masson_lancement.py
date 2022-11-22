from projet2_masson_fonction import *


url_general="https://books.toscrape.com"
#url_actuel_categorie = "https://books.toscrape.com/catalogue/category/books/sequential-art_5/index.html" # défini le nom du site dans la variable url
url_actuel_categorie="https://books.toscrape.com/catalogue/category/books/erotica_50/index.html"
#url_actuel_categorie="https://books.toscrape.com/catalogue/category/books/fiction_10/index.html"
#url_actuel_categorie="https://books.toscrape.com/catalogue/category/books/romance_8/index.html"

#------- Définir l'ordre des colonnes CSV
liste_entete=[
    "image",
    "url",
    "upc",
    "title",
    "tax",
    "no_tax",
    "availability",
    "description",
    "category",   
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
nom_du_csv="export_livre02"

#------ Initialisation du fichier csv
creation_csv(liste_entete, dico_entete,nom_du_csv)


#------ lancement de la fonction pour exporter les catégories
dico_categorie={}# Création d'un dico vide pour les URL des categories
lancement_export_categorie(url_general,dico_categorie)#Lance le programme

for key_categorie in dico_categorie:
    liste_ouvrage_categorie=[] #Création d'un liste vide pour les ouvrages    
    url_actuel_categorie=dico_categorie[key_categorie] #Défini l'URL de la catégorie en cours
    
#------ Export des livres par catégorie
    lancement_export_ouvrage(url_general,url_actuel_categorie, liste_ouvrage_categorie)#lancement du programme
    print ("Analyse de la catégorie ", key_categorie," en cours", " \n "
           "Il y a ", len(liste_ouvrage_categorie),"livres dans cette categorie")
#------ Lancement de la boucle pour chaque livre de la catégorie en cours
    nbr=1 #Compteur pour l'avancée du chargement
    for livre in liste_ouvrage_categorie:
        url_courant_livre=livre #Défini le livre en cours
        analyse_livre(liste_entete,dico_entete,url_general,url_courant_livre,nom_du_csv) #Lance le programme
    
        print("analyse du livre ", nbr ," / ", len(liste_ouvrage_categorie))# Barre d'avancée
        nbr += 1

print("Fin de l'analyse")#Fin du programme