import requests
import json
from bs4 import BeautifulSoup

URLS    = ['https://platzi.com/p/danielpedroza/', 'https://platzi.com/p/pedrozad/', 'https://platzi.com/p/danielalbertopedrozaacua/', 'https://platzi.com/p/carlospedroza/']
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}

#danielalbertopedrozaacua
#danielpedroza
#pedrozad
#carlospedroza
def parse_home():
    for url in URLS:
        try:
            response = requests.get(url,HEADERS)

            if response.status_code == 200:
                soup    = BeautifulSoup(response.content, 'html.parser')
                # This here is the secret, it has to search into the Ctrl+U code of the page to see wich script are the correct, in this case was 18 but index start on zero
                script  = soup.find_all('script')[17]
                script  = script.string.strip()
                
                # name:
                start   = script.find(" name: ")#+8
                end     = script.find(" avatar:")
                name    = script[start:end]

                # points:
                start   = script.find(" points:")#+10
                end     = script.find(" questions:")
                points  = script[start:end]

                # Output
                print(name, points)
        
            else:
                raise ValueError(f'Error: {response.status_code}')

        except ValueError as ve:
            print (ve)


def run():
    parse_home()


if __name__ == '__main__':
    run()
