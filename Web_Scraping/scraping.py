import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/news')
res2 = requests.get('https://news.ycombinator.com/news?p=2')
soup = BeautifulSoup(res.text, 'html.parser')
soup2 = BeautifulSoup(res2.text, 'html.parser')
links = soup.select('.storylink')
links2 = soup2.select('.storylink')
subtext = soup.select('.subtext')
subtext2 = soup2.select('.subtext')


def sort_stories_by_score(hnlist):
    return sorted(hnlist, key=lambda hnlist: hnlist['points'], reverse=True)


def create_custom_hn(_links, _subtext):
    hn = []
    for idx, item in enumerate(links):
        title = _links[idx].getText()
        href = _links[idx].get('href', None)
        score = _subtext[idx].select('.score')
        if len(score):
            point = int(score[0].getText().replace(' points', ''))
            if point > 99:
                dickie = {'title': title, 'href': href, 'points': point}
                hn.append(dickie)
    return hn


result = create_custom_hn(links, subtext) + create_custom_hn(links2, subtext2)
sorted_result = sort_stories_by_score(result)

pprint.pprint(sorted_result)
