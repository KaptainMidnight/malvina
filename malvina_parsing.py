import requests
from bs4 import BeautifulSoup as bs


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; rv:47.0) Gecko/20100101 Firefox/47.0',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}

b_url = 'http://malvina-club.ru/hours/'


def girl_pars():

    session = requests.Session()
    request = session.get(b_url, headers=headers)

    if request.status_code == 200:

        soup = bs(request.content, "lxml")
        hours_table = soup.find('table', attrs={'id': 'hours_table'})

        girls_info = hours_table.find_all('tr', attrs={'class': 'hours'})

        for girl in girls_info:
            hours = [x['data-hours'] for x in girl.find_all("td", {'data-rest': 'false'})]
            date = [x['data-date'] for x in girl.find_all("td", {'data-rest': 'false'})]
            work_time = dict(zip(date, hours))

            data = {
                'name': girl.span.text,
                'work_time': work_time,
                'foto': girl.img['src']
            }

        return data
