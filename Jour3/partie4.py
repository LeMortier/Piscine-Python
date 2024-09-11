from bs4 import BeautifulSoup
from html import fetch_html

def get_one_book() -> dict:
   
    html_doc = BeautifulSoup(fetch_html("https://books.toscrape.com/"), "html.parser")
    book = html_doc.find("article")
    result = {}
    result["title"]=book.find("h3").text
    result["rating"]=len(book.find_all(name="i", class_="icon-star"))
    result["price"]=float(book.find(name="p", class_="price_color").text[2:])
    return result

def get_one_book_complete() -> dict:
   
    html_doc = BeautifulSoup(fetch_html("https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"), "html.parser")
    book = html_doc.find("article")
    result = {}
    result["title"]=book.find("h1").text
    result["rating"] = len(book.find_all(name="i", class_="icon-star"))
    result["price"] = float(book.find(name="p", class_="price_color").text[2:])
    result["description"] = book.find_all("p")[-1].text
    return result

def get_page_books(url: str | None=None) -> list[dict]:
   
    if not url:
        url_to_scrape = "https://books.toscrape.com/?"
    else:
        url_to_scrape = url
    home = BeautifulSoup(fetch_html(url_to_scrape), "html.parser")
    result = []
    
    titles = home.find_all("h3")
    for title in titles:
        link = "{}.com{}".format(url_to_scrape.split(".com")[0],title.find("a")["href"])
        html_book = BeautifulSoup(fetch_html(link), "html.parser")
        book = html_book.find("article")
        data = {}
        data["title"] = book.find("h1").text
        data["rating"] = len(book.find_all(name="i", class_="icon-star"))
        data["price"] = float(book.find(name="p", class_="price_color").text[2:])
        
        for p in book.find_all("p"):
            if not p.attrs:
                data["description"] = p.text
        result.append(data)
    if not url:
        result += get_page_books("https://books.toscrape.com/catalogue/page-5.html")
    return result
