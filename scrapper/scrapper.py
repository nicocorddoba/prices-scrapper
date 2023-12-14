import requests
from bs4 import BeautifulSoup as bs

def ml_scrapper(ml_content) -> list[tuple]:
    """Obtains the price, link and title of three different products from mercadolibre's page

    Args:
        ml_content (_type_): content of mercadolibre's page to scrapp

    Returns:
        pdata (list[tuple]): list of the three products
    """
    content = bs(ml_content,'html.parser')
    plist = content.find_all('div', {'class':'ui-search-result__wrapper'})
    pdata = []
    for i in range(3):
        pdict = {}
        pdict['title'] = plist[i].find_all('h2', {'class':'ui-search-item__title'})[0].text
        pdict['price'] = plist[i].find_all('span', {'class':'andes-money-amount__fraction'})[0].text
        pdict['link'] = plist[i].find_all('a', {'class':'ui-search-item__group__element ui-search-link__title-card ui-search-link'})[0].get('href')
        pdata.append(pdict)
    return pdata


def mexx_scrapper(mexx_content) -> list[tuple]:
    """Obtains the price, link and title of three different products from mexx's page

    Args:
        mexx_content (_type_): content of mexx's page to scrapp

    Returns:
        pdata (list[tuple]): list of the three products
    """
    content = bs(mexx_content,'html.parser')
    plist = content.find_all("div",{"class":"card-body px-3 pb-0 pt-0"})
    pdata = []
    for i in range(3):
        pdict = {}
        pdict['title'] = plist[i].find_all("h4", {"class":"card-title mb-1 h-40"})[0].text
        pdict['price'] = plist[i].find_all("h6", {"class":"mb-0 anterior"})[0].text
        pdict['link'] = plist[i].find_all("h4", {"class":"card-title mb-1 h-40"})[0].find('a').get('href')
        pdata.append(pdict)
    return pdata