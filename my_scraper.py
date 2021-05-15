import requests
from bs4 import BeautifulSoup as soup


my_url = "http://books.toscrape.com/catalogue/category/books/autobiography_27/index.html"

r = requests.get(my_url)

page_soup = soup(r.content, "html.parser")

books = page_soup.find_all(class_="col-xs-6 col-sm-4 col-md-3 col-lg-3")

filename = "books.csv"
headers = "book_title, book_price, book_rating, book_availability\n"
with open(filename, "w") as f:

    f.write(headers)

    for book in books:
        
        book_title = book.h3.a["title"]
        book_price = book.find(class_="product_price")
        book_color = book_price.find(class_="price_color").get_text()
        book_availability = book_price.find(class_="instock availability").get_text().strip()
        book_rate = book.p["class"]
        book_rating = " ".join(book_rate)

        print("Book Title: " + book_title)
        print("Book Price: " + book_color)
        print("Book Rating: " + book_rating)
        print("Book Availability: " + book_availability)
        

        f.write(book_title.replace(",", "|") + "," + book_color + "," + book_rating + "," + book_availability + "\n")
       
        
