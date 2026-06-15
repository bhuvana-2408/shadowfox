import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com/"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    quotes = soup.find_all("span", class_="text")

    print("Quotes extracted from website:\n")

    for i, quote in enumerate(quotes, start=1):
        print(f"{i}. {quote.text}")

else:
    print("Failed to retrieve the webpage.")