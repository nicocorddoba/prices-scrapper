import requests
from scrapper.scrapper import mexx_scrapper, ml_scrapper
from prettytable import PrettyTable


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
    mltable = PrettyTable()
    mltable.field_names = ["Title", "Price", "Link"]
    mexxtable = PrettyTable()
    mexxtable.field_names = ["Title", "Price", "Link"]
    for i in range(3):
        mltable.add_row([ml_products[i]['title'],
                         ml_products[i]['price'],
                         ml_products[i]['link']])
        mexxtable.add_row([mexx_products[i]['title'],
                           mexx_products[i]['price'],
                           mexx_products[i]['link']])
    print(mltable, mexxtable)
    


if __name__ == "__main__":
    main()
