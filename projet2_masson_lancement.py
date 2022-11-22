from projet2_masson_fonction import *

url_general="https://books.toscrape.com"
#url_actuel_categorie = "https://books.toscrape.com/catalogue/category/books/sequential-art_5/index.html" # défini le nom du site dans la variable url
url_actuel_categorie="https://books.toscrape.com/catalogue/category/books/erotica_50/index.html"
#url_actuel_categorie="https://books.toscrape.com/catalogue/category/books/fiction_10/index.html"
url_actuel_categorie="https://books.toscrape.com/catalogue/category/books/romance_8/index.html"

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

liste_ouvrage_categorie=[]    

#------ Export des livres par catégorie
lancement_export_ouvrage(url_general,url_actuel_categorie, liste_ouvrage_categorie)

for livre in liste_ouvrage_categorie:
    url_courant_livre=livre
    print(url_courant_livre)
    analyse_livre(liste_entete,dico_entete,url_general,url_courant_livre,nom_du_csv)


print("Fin de l'analyse")