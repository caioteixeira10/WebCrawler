import requests
import lxml
from bs4 import BeautifulSoup
import re
import sys
import multiprocessing as mp
from multiprocessing import Pool

# ######################################################
# Author : Caio Teixeira Bastone
# email : caiotbastone@gmail.com
# Date : April 2nd, 2022
# ######################################################

def main(url):
    list_links = getLinks(url)
    pool = mp.Pool()
    for i in list_links:
        print(f"Fetching from {i}")
        new_urls = getLinks(i)
        # async_content = pool.apply_async(getLinks, args = (i, ), callback = printFunction ) 
        if not new_urls:
            print("\tThe url does not contain any url to be fetched")
        else:
            for j in new_urls:
                print(f'\t{j}')
                
### Implement Parallelization 
# def printFunction(new_urls):
#     if not new_urls:
#         print("\tThe url does not contain any url to be fetched")
#     else:
#         for j in new_urls:
#             print(f'\t{j}')
            
def getLinks(url):
    f = requests.get(url)
    soup = BeautifulSoup(f.text, 'html.parser')
    urls = []
    regex = "(?P<url>https?://[rescale.com]+)"
    for link in soup.find_all('a'):
        url = str(link.get('href'))
        match = re.search(regex, url)
        if match is not None:
            urls.append(url)
    return urls
    
   
if __name__ == "__main__": 
    url = str(sys.argv[1])
    main(url)
