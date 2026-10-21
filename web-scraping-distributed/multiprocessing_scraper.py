import sys
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup, Tag, NavigableString
import pickle
from multiprocessing import Pool, cpu_count

# Définition des fonctions
##########################

def get_bsobj_from_url(url):
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    req = Request(url,headers={'User-Agent':user_agent})
    try:
        response = urlopen(req)
    except (HTTPError, URLError) as e:
        sys.exit(e)
    return BeautifulSoup(response, 'lxml')

def get_name(bsobj):
    return bsobj.find("h1", class_="notice__title h_1").get_text()

def get_section_info(bsobj):
    return bsobj.find("section", class_="notice__fullcartel wrap")

def extract_text(soup):
    texte = ""
    # boucle sur les enfants de soup
    for c in soup.children:
        # si l'enfant est un NavigableString : on récupère le texte
        # dans c.string, et on retire les espaces en trop (.strip())
        if type(c) == NavigableString:
            if (c.string).strip() != "":
                texte += " "+(c.string).strip()
        # si l'enfant est un tag qui n'est pas un bouton (balise button)
        # on va chercher le texte à l'intérieur et on le rajoute au texte déjà récupéré
        elif type(c) == Tag and c.name != "button" :  
            texte += extract_text(c)

    return texte

def parse_url(url):
    bsobj = get_bsobj_from_url(url)
    return (url, get_name(bsobj), extract_text(bsobj))

def build_url_list(url, url_base):
    bs = get_bsobj_from_url(url)
    oeuvres = bs.find_all("article", class_="card--search")
    ls = []
    for oeuvre in oeuvres:
        ls.append(url_base+oeuvre.find("a", class_="square-content card__img__inner").attrs["href"])
    return ls

def build_all_url_list(url, url_base):
    bs = get_bsobj_from_url(url)
    ls = []
    for page in range(int(bs.find("span", class_="pagination__total nav__pagination__nbr").get_text())):
        url_page = url_base + '/recherche?page='+str(page+1)+ '&' + url.split("recherche?")[1]
        ls.extend(build_url_list(url_page, url_base))
    return ls

# Programme principal
#####################
if __name__ == '__main__':
    # Question 1.1
    louvre = get_bsobj_from_url('https://collections.louvre.fr/ark:/53355/cl010096624')
    # print(louvre.prettify())

    # Question 1.2
    # print(get_name(louvre))

    # Question 1.3
    # print(get_section_info(louvre))
    # print(type(get_section_info(louvre)))

    # Question 1.4
    louvre_section_info = get_section_info(louvre)
    # print(extract_text(louvre_section_info))s

    # Question 1.5
    # print(parse_url('https://collections.louvre.fr/ark:/53355/cl010096624'))
    # print(type(parse_url('https://collections.louvre.fr/ark:/53355/cl010096624')))
    # print(parse_url('https://collections.louvre.fr/ark:/53355/cl010096628'))

    # Question 2.1
    # print(build_url_list('https://collections.louvre.fr/recherche?limit=20&location%5B0%5D=141080&typology%5B0%5D=11', 'https://collections.louvre.fr'))

    # Question 2.2
    # print(build_all_url_list('https://collections.louvre.fr/recherche?limit=20&location%5B0%5D=141080&typology%5B0%5D=11', 'https://collections.louvre.fr'))

    # Question 2.3
    # all_urls = build_all_url_list('https://collections.louvre.fr/recherche?limit=20&location%5B0%5D=141080&typology%5B0%5D=11', 'https://collections.louvre.fr')
    # arts_du_livre = []
    # for url in all_urls:
    #     arts_du_livre.append(parse_url(url))
    
    # Question 2.4
    # with open('arts_du_livre.pick', 'wb') as pickFile:
        # pickle.dump(arts_du_livre, pickFile)

    # Question 2.5
    all_urls_peintures = build_all_url_list('https://collections.louvre.fr/recherche?limit=20&location[0]=190540&typology[0]=22', 'https://collections.louvre.fr')
    print(all_urls_peintures)