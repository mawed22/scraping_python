import requests
from bs4 import BeautifulSoup

url = "https://codeavecjonathan.com/scraping/techsport/"

def get_text_if_not_none(e):
    if e:
        return e.text.strip() #.strip() Permet d'eliminer les espaces avant et apres la chaine de caracteres
    return None


response = requests.get(url)
response.encoding = response.apparent_encoding

if response.status_code == 200 :
    html = response.text
    #print(html)

    f = open("recette.html", "w")
    f.write(html)
    f.close()

    soup = BeautifulSoup(html, 'html5lib')

    titre = get_text_if_not_none(soup.find("h1"))
    print(titre)

    description = get_text_if_not_none(soup.find("p", class_="description"))
    print(description)

    #Ingredients
    div_ingredients = soup.find("div", class_="ingredients")
    e_ingredients = div_ingredients.find_all("p")
    for e_ingredient in e_ingredients:
        print("INGREDIENT", e_ingredient.text)

    #Preparation
    table_preparations = soup.find("table", class_="preparation")
    e_preparations = table_preparations.find_all("td", class_="preparation_etape")
    i = 0
    for e_preparation in e_preparations:
        i=i+1
        print("Etape", str(i),":", e_preparation.text)


else :
    print('Erreur:', response.status_code)