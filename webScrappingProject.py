import requests
from bs4 import BeautifulSoup

data = requests.get('https://rahulshettyacademy.com/AutomationPractice/')
soup = BeautifulSoup(data.content, 'html.parser')
#print(soup.prettify())
soup_table = soup.find('table', {'class': 'table-display'})
# print(soup_table.prettify())
for each in soup_table:
    soup_table_rows = soup_table.findAll('tr')
    # print(soup_table_rows)
    for each_row in soup_table_rows[1:]:
        # print(each_row)
        rows_data = each_row.findAll('td')
        # print(rows_data)
        for row_data in rows_data:
            print(row_data.text)

