import requests
from bs4 import BeautifulSoup


# the variable is stored for all players info
all_players = {}

# the vatiable for get_html_content function
result_html = [] 

urls = []

def main():
    get_html_contents()

def get_html_contents():
    url = "https://www.realmadrid.com/ja/football/squad"
    html = requests.get(url)
    soup = BeautifulSoup(html.content, "html.parser")
    source = soup.find_all(class_='m_player_info_content')
    for x in source:
        tag = x.find("a", itemprop="url")
        try:
            urls.append("https://www.realmadrid.com" + tag.get("href"))
        except AttributeError:
            pass

    return urls


def get_positions():
    for url in urls:
        html = requests.get(url)
        soup = BeautifulSoup(html.content, "html.parser")
        #source = soup.find_all("span", class_ = "name")
        #print([ x.text for x in source ])

        source1 = soup.find_all("div", class_= "data_info")
        print("#############")
        for x in source1:
            print(x.text)
get_html_contents()
get_positions()



