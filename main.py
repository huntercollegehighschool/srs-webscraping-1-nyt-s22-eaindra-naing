from bs4 import BeautifulSoup
import urllib.request

def get_headlines():
    r = urllib.request.urlopen("https://www.nytimes.com/")  # returns html of the website

    soup = BeautifulSoup(r, "html.parser") #parse html

    headlines = []

    links = soup.find_all("a") # all codes with tag "a"

    for link in links:
      header = link.find("h3") # h3 = headlines finding out of a tags
      if headline != None:
        print(headline.text)

    return headlines
 
  
def get_links():

    r = urllib.request.urlopen("https://www.nytimes.com/")  # returns html of the website

    soup = BeautifulSoup(r, "html.parser") #parse html

    articles = []

    return articles
    
#print(get_headlines())
print(get_links())