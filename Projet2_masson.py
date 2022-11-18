import requests # Permet de faire des requetes sur Internet
import re # Permet d'exporter un nombre d'un string
from bs4 import BeautifulSoup # Permet de faire du WebScrapping

url = "http://books.toscrape.com/catalogue/ms-marvel-vol-1-no-normal-ms-marvel-2014-2015-1_34/index.html" # défini le nom du site dans la variable url
page = requests.get(url) # défini la variable qui appel le site
soup = BeautifulSoup(page.content, "html.parser") #Initialise le fichier

#------- Creait un dico vide avec les informations de l'album
dico_courant={}


#------- Récupére le product_page_url .....
#------- Récupére le image_url
#------- Mettre les valeurs dans un dictionnaire

#------- Récupére le title
balise_title=soup.find("div", class_="col-sm-6 product_main") # Recherche le paragraphe du titre
balise_title=balise_title.find("h1")# Recherche le titre h1 dans le paragraphe
balise_title=balise_title.get_text()# Extrait le texte du titre h1
dico_courant["title"]=balise_title

#------- Récupére le product_description
balise_description=soup.find("div", id="product_description")# Recherche le paragraphe de la description
balise_description=balise_description.find_next("p")#Recherche le paragraphe principale situé après
balise_description=balise_description.get_text()#Extrait le texte du paragraphe
dico_courant["desription"]=balise_description


#------- Récupére le category
balise_category=soup.find("ul",class_="breadcrumb") #Recherche le chemin de fer de la localisation
for balise in balise_category: #Parcours les différentes balises
    if balise.get_text()==balise_title: #Recherche le dernier titre du chemin de fer
        balise_category=balise.find_previous_sibling() #Récupére la balise précédente
        balise_category=balise_category.get_text() #Récupére juste le texte
        balise_category=balise_category[1:-1]#Supprime le retour à la ligne du début et de la fin
        dico_courant["category"]=balise_category


balises_th = soup.find_all('th') #Recherche toutes les balises th
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
         
#------ Met le dico courant dans un dico spécial pour l'album
globals()['dico_%s' % balise_title] = dico_courant 