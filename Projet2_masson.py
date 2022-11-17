import requests # appel le package requests
from bs4 import BeautifulSoup

url = "http://books.toscrape.com/catalogue/ms-marvel-vol-1-no-normal-ms-marvel-2014-2015-1_34/index.html" # défini le nom du site dans la variable url
page = requests.get(url) # défini la variable qui appel le site
soup = BeautifulSoup(page.content, "html.parser")



texts = soup.find_all('th')
for text in texts:
    if text.get_text() == "Product Type":
        temp=text.find_next()
        temp2=temp.get_text()
        print (temp2)
    

   # If soup.get_text()=="UPC":
    #    test=soup.find_next(th)

# affiche toutes les balises "a"
#soup.get_text()# récupère tout le texte

#print(test)
