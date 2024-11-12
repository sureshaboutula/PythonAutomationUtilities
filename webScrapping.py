import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

data = requests.get('https://www.imdb.com/find/?q=thriller&ref_=nv_sr_sm', headers=headers)
soup = BeautifulSoup(data.content, 'html.parser')
# print(soup.prettify())
table = soup.find('ul', {'class': 'ipc-metadata-list ipc-metadata-list--dividers-after sc-e8e4ce7-3 dTEYDP ipc-metadata-list--base'})
#print(table.prettify())
rows = table.findAll('li')
for row in rows:
    #print(row.prettify())
    rowsdata = row.findAll('div', {'class': 'ipc-metadata-list-summary-item__c'})
    for rowdata in rowsdata:
        rowsdata_div = rowdata.findAll('div', {'class': 'ipc-metadata-list-summary-item__tc'})
        for rowdata_div in rowsdata_div:
            rowdata_div_a = rowdata_div.findAll('a')
            suburl = rowdata_div_a[0]['href']
            subdata = requests.get("https://www.imdb.com"+suburl, headers=headers)
            print(subdata.text)
            # subSoup = BeautifulSoup(subdata.content, 'html.parser')
            # print(subSoup.prettify())
            # # subSoupData = subSoup.find('div', {'class':'sc-3c16af05-0 kefoZk'})
            # # print(subSoupData)


