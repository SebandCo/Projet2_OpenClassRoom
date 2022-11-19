import requests # Permet de faire des requetes sur Internet
from bs4 import BeautifulSoup # Permet de faire du WebScrapping
from urllib.parse import urljoin # Permet de fusionner deux URL ensemble

url_general="https://books.toscrape.com"
url2 = "https://books.toscrape.com/catalogue/category/books/sequential-art_5/index.html" # défini le nom du site dans la variable url
#url2="https://books.toscrape.com/catalogue/category/books/erotica_50/index.html"
page2 = requests.get(url2) # défini la variable qui appel le site
soup2 = BeautifulSoup(page2.content, "html.parser")

#------- Crée une liste avec la liste des ouvrages par catégorie
       
liste_ouvrage_categorie=[]    
for balise in soup2.find_all('a'): # Balaie tout les liens
    if balise.get("title"): # Récupere les liens avec un titre--> Hors image
        url_provisoire=balise['href'] #Récupere l'URL du livre
        balise_url=urljoin(str(url_general), str(url_provisoire)) #Fusionne les deux URL
        liste_ouvrage_categorie.append(balise_url)# Rajout des URL à la liste générale


if not soup2.find("ul",class_="pager"): # Vérifie que le bandeau de changement de page existe
    print("Une seule page")
else:
    print("Deux page")