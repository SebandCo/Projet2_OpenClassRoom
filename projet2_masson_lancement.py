from projet2_masson_fonction import *

url_general="https://books.toscrape.com"
url_courant = "http://books.toscrape.com/catalogue/ms-marvel-vol-1-no-normal-ms-marvel-2014-2015-1_34/index.html" # défini le nom du site dans la variable url
url_courant = "https://books.toscrape.com/catalogue/sapiens-a-brief-history-of-humankind_996/index.html"
url_courant = "https://books.toscrape.com/catalogue/rat-queens-vol-3-demons-rat-queens-collected-editions-11-15_921/index.html"

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



creation_csv(liste_entete, dico_entete,nom_du_csv)
analyse_livre(liste_entete,dico_entete,url_general,url_courant,nom_du_csv)# Lance l'analyse d'un livre à partir de l'URL courant