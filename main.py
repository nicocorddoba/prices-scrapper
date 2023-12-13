import requests
import bs4


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
    cg_url = "https://compragamer.com/?seccion=3&criterio="
    cg_order = "&sort=lower_price"
    inpt:str = inpt
    search_ml = inpt.replace(' ','-')
    search_cg = inpt.replace(' ','%20')
    return [ml_url + search_ml + ml_order, cg_url + search_cg + cg_order]


def main():
    inpt:str = input("What are you looking for?: ")
    slist = search(inpt=inpt)
    ml_content = get_request(slist[0])
    cg_content = get_request(slist[1])


if __name__ == "__main__":
    main()
