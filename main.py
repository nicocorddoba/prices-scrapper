import requests
from scrapper.scrapper import mexx_scrapper, ml_scrapper

def get_request(url:str) -> str:
    """Simply function to get the content of a page

    Args:
        url (str): url of the page to get scrapped

    Returns:
        content: content of the page
    """
    request = requests.get(url=url)
    content = request.content
    return content


def search(inpt: str)->list:
    """Creates a list of search inputs for a given search term

    Args:
        inpt (str): search term given

    Returns:
        list: list of urls to get scrapped 
    """
    ml_url = "https://listado.mercadolibre.com.ar/"
    ml_order = "_OrderId_PRICE_NoIndex_True"
    mexx_url = "https://www.mexx.com.ar/buscar/?"
    mexx_order = "precio=menor&p="
    inpt:str = inpt
    search_ml = inpt.replace(' ','-')
    search_mexx = inpt.replace(' ','%20')
    return [ml_url + search_ml + ml_order, mexx_url + mexx_order + search_mexx]


def main():
    inpt:str = input("What are you looking for?: ")
    slist = search(inpt=inpt)
    ml_content = get_request(slist[0])
    mexx_content = get_request(slist[1])
    ml_products = ml_scrapper(ml_content)
    mexx_products = mexx_scrapper(mexx_content)
    for i in range(3):
        print(ml_products[i]['title'], end=' --------- ')
        print(mexx_products[i]['title'])
        print(ml_products[i]['price'], end=' --------- ')
        print(mexx_products[i]['price'])
        print(ml_products[i]['link'], end=' --------- ')
        print(mexx_products[i]['link'], end='\n \n')
    


if __name__ == "__main__":
    main()
