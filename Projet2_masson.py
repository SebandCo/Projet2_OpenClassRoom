import requests # Permet de faire des requetes sur Internet
import re # Permet d'exporter un nombre d'un string
from bs4 import BeautifulSoup # Permet de faire du WebScrapping
import csv # Permet de transférer des données vers un fichier csv
from urllib.parse import urljoin # Permet de fusionner deux URL ensemble

url_general="https://books.toscrape.com"
url = "http://books.toscrape.com/catalogue/ms-marvel-vol-1-no-normal-ms-marvel-2014-2015-1_34/index.html" # défini le nom du site dans la variable url
url = "https://books.toscrape.com/catalogue/sapiens-a-brief-history-of-humankind_996/index.html"
page = requests.get(url) # défini la variable qui appel le site
soup = BeautifulSoup(page.content, "html.parser") #Initialise le fichier



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

#-----------------Boucle possible à partir d'ici--------------------------

#------- Creait un dico vide avec les informations de l'album
dico_courant={}


#------- Récupére le product_page_url .....
dico_courant["url"]="URL Vide"

#------- Récupére le title
balise_title=soup.find("div", class_="col-sm-6 product_main") # Recherche le paragraphe du titre
balise_title=balise_title.find("h1")# Recherche le titre h1 dans le paragraphe
balise_title=balise_title.get_text()# Extrait le texte du titre h1
dico_courant["title"]=balise_title

#------- Récupére le product_description
balise_description=soup.find("div", id="product_description")# Recherche le paragraphe de la description
balise_description=balise_description.find_next("p")#Recherche le paragraphe principale situé après
balise_description=balise_description.get_text()#Extrait le texte du paragraphe
dico_courant["description"]=balise_description


#------- Récupére le category
balise_category=soup.find("ul",class_="breadcrumb") #Recherche le chemin de fer de la localisation
for balise in balise_category: #Parcours les différentes balises
    if balise.get_text()==balise_title: #Recherche le dernier titre du chemin de fer
        balise_category=balise.find_previous_sibling() #Récupére la balise précédente
        balise_category=balise_category.get_text() #Récupére juste le texte
        balise_category=balise_category[1:-1]#Supprime le retour à la ligne du début et de la fin
        dico_courant["category"]=balise_category


balises_th = soup.find_all("th") #Recherche toutes les balises th
for balise in balises_th: #Parcours toutes les balises th trouvées
#------- Récupére le universal_product_code (upc)
    if  balise.get_text() == "UPC": #Si la balise th s'appelle UPC
        upc_balise=balise.find_next() #Récupere la balise suivante
        upc_balise=upc_balise.get_text() #Récupere juste le texte
        dico_courant["upc"]=upc_balise
        
#------- Récupére le prince_excluding_tac
    elif  balise.get_text() == "Price (excl. tax)": #Si la balise th s'appelle Price (excl. tax)
         price_no_tax_balise=balise.find_next() #Récupere la balise suivante
         price_no_tax_balise=price_no_tax_balise.get_text() #Récupere juste le texte
         dico_courant["no_tax"]=price_no_tax_balise
            
#------- Récupére le price_including_tax
    elif  balise.get_text() == "Price (incl. tax)": #Si la balise th s'appelle Price (incl. tax)
         price_tax_balise=balise.find_next() #Récupere la balise suivante
         price_tax_balise=price_tax_balise.get_text() #Récupere juste le texte
         dico_courant["tax"]=price_tax_balise   

#------- Récupére le number_available
    elif  balise.get_text() == "Availability": #Si la balise th s'appelle Availability
         availability_balise=balise.find_next() #Récupere la balise suivante
         availability_balise=availability_balise.get_text() #Récupere juste le texte
         availability_balise=re.findall("\d+",availability_balise)[0] #Récupère le nombre dans le texte
         dico_courant["availability"]=availability_balise 
         
#------- Récupére le review_rating
    elif  balise.get_text() == "Number of reviews": #Si la balise th s'appelle Number of reviews
         review_balise=balise.find_next() #Récupere la balise suivante
         review_balise=review_balise.get_text() #Récupere juste le texte
         dico_courant["review"]=review_balise
         
#------- Récupére le image_url
for image in soup.findAll("img"): # Balaie toutes les balises pour trouver les images
    if image.get('alt', '') == balise_title:# Recherche la balise correspondant au livre en cours
        balise_url_provisoire=image['src']# Récupere l'adresse src de l'image

balise_url=urljoin(str(url_general), str(balise_url_provisoire)) #Fusionne les deux URL
dico_courant["image"]=balise_url

#------- Récupére le fichier image

nom_livre=re.split('/', url)
f = open(nom_livre[-2]+".jpg",'wb')
response = requests.get(balise_url)
f.write(response.content)
f.close()
         
#------ Met le dico courant dans un dico spécial pour l'album
globals()['dico_%s' % balise_title] = dico_courant #Copie le dico courant dans le dico général
liste_ouvrage=[balise_title] #Creait un liste avec tous les noms d'ouvrage

#-----------------Fin de la boucle possible à partir d'ici--------------------------

#-----------------Export dans un fichier csv--------------------------
#------ Mise en place des entêtes
liste_entete_csv_export=[] # Création d'une liste vide pour déverser les valeurs dans le fichier CSV
for key in liste_entete: # Parcourir la liste pour définir l'ordre des entêtes
    liste_entete_csv_export.append(dico_entete[key]) # Création d'une liste pour déverser dans le CSV
        
with open('export_livre.csv','w',newline='') as fichiercsv: # Création d'un fichier CSV
    writer = csv.writer(fichiercsv,delimiter=',')
    writer.writerow(liste_entete_csv_export)# Deverse les lignes dans le fichier

#------ Mise en place des champs
liste_ouvrage_csv_export=[] # Création d'une liste vide pour déverser les valeurs dans le fichier CSV
for key in liste_entete:# Parcourir la liste pour définir l'ordre des valeurs
    liste_ouvrage_csv_export.append(globals()['dico_%s' % balise_title][key])# Création d'une liste pour déverser dans le CSV
    
        
with open('export_livre.csv','a',newline='') as fichiercsv: # Réutilise le fichier CSV
    writer = csv.writer(fichiercsv,delimiter=',')
    writer.writerow(liste_ouvrage_csv_export)# Deverse les lignes dans le fichier



for key,value in dico_entete.items():
    print(key, ':', value)