import requests # Permet de faire des requetes sur Internet
import re # Permet d'exporter un nombre d'un string
from bs4 import BeautifulSoup # Permet de faire du WebScrapping

url = "http://books.toscrape.com/catalogue/ms-marvel-vol-1-no-normal-ms-marvel-2014-2015-1_34/index.html" # défini le nom du site dans la variable url
page = requests.get(url) # défini la variable qui appel le site
soup = BeautifulSoup(page.content, "html.parser") #Initialise le fichier


#------- Récupére le product_page_url .....
#------- Récupére le product_desciption
#------- Récupére le category
#------- Récupére le image_url
#------- Mettre les valeurs dans un dictionnaire

#------- Récupére le title
balise_title=soup.find("div", class_="col-sm-6 product_main") # Recherche le paragraphe du titre
balise_title=balise_title.find("h1")# Recherche le titre h1 dans le paragraphe
balise_title=balise_title.get_text()# Extrait le texte du titre h1
print(balise_title)


balises_th = soup.find_all('th') #Recherche toutes les balises th
for balise in balises_th: #Parcours toutes les balises th trouvées
#------- Récupére le universal_product_code (upc)
    if  balise.get_text() == "UPC": #Si la balise th s'appelle UPC
        upc_balise=balise.find_next() #Récupere la balise suivante
        upc_balise=upc_balise.get_text() #Récupere juste le texte
        print (upc_balise)
#------- Récupére le prince_excluding_tac
    elif  balise.get_text() == "Price (excl. tax)": #Si la balise th s'appelle Price (excl. tax)
         price_no_tax_balise=balise.find_next() #Récupere la balise suivante
         price_no_tax_balise=price_no_tax_balise.get_text() #Récupere juste le texte
         print (price_no_tax_balise)
            
#------- Récupére le price_including_tax
    elif  balise.get_text() == "Price (incl. tax)": #Si la balise th s'appelle Price (incl. tax)
         price_tax_balise=balise.find_next() #Récupere la balise suivante
         price_tax_balise=price_tax_balise.get_text() #Récupere juste le texte
         print (price_tax_balise)   

#------- Récupére le number_available
    elif  balise.get_text() == "Availability": #Si la balise th s'appelle Availability
         availability_balise=balise.find_next() #Récupere la balise suivante
         availability_balise=availability_balise.get_text() #Récupere juste le texte
         availability_balise=re.findall("\d+",availability_balise)[0] #Récupère le nombre dans le texte
         print (availability_balise) 
         
#------- Récupére le review_rating
    elif  balise.get_text() == "Number of reviews": #Si la balise th s'appelle Number of reviews
         review_balise=balise.find_next() #Récupere la balise suivante
         review_balise=review_balise.get_text() #Récupere juste le texte
         print (review_balise)