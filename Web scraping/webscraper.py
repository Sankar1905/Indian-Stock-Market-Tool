from bs4 import BeautifulSoup as soup  # HTML data structure
from urllib.request import Request, urlopen as uReq  # Web client

# URl to web scrap from.
# in this example we web scrap graphics cards from Newegg.com
page_urls = ["https://www.moneycontrol.com/india/stockpricequote/miscellaneous/irctc-indianrailwaycateringtourismcorp/IRC",
"https://www.moneycontrol.com/india/stockpricequote/banks-private-sector/yesbank/YB",
"https://www.moneycontrol.com/india/stockpricequote/refineries/relianceindustries/RI"]
for page_url in page_urls:
    req = Request(page_url, headers={'User-Agent': 'Mozilla/5.0'})

    # opens the connection and downloads html page from url
    uClient = uReq(req)

    # parses html into a soup data structure to traverse html
    # as if it were a json data type.
    page_soup = soup(uClient.read(), "html.parser")
    uClient.close()
    stock_name_container = page_soup.find(id="stockName")
    stock_name = stock_name_container.h1.text
    print(stock_name)
    price_value_container = page_soup.findAll("div", {"id": "nsecp"})
    price_value = price_value_container[0].text
    print(price_value)
    price_container = page_soup.findAll("input", {"id": "nsespotval"})
    stock_details_container = price_container[0]
    stock_update_time = stock_details_container.p.text
    print(stock_update_time)
    gain_loss_value = stock_details_container.div.text
    print(gain_loss_value)
    
