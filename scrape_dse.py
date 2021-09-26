# imports
import requests
from bs4 import BeautifulSoup


def clean_td(td: str) -> str:
    # cleans the table data
    return td.text.strip().replace(",", "")


def scrape_dse(start_date, end_date):
    URL = (f"https://www.dsebd.org/day_end_archive.php?startDate={start_date}&" +
           f"endDate={end_date}&inst=All%20Instrument&archive=data")
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')

    table = soup.find('div', class_='table-responsive')
    rows = table.find_all('tr')[1:]

    td_list = list()
    for row in rows:
        table_data = row.find_all('td')[1:]
        td_list.append(tuple(clean_td(td) for td in table_data))

    with open('2021.csv', 'a') as f:
        for row in td_list:
            f.write(row[1]+','+row[0]+','+row[5]+',' +
                    row[3]+','+row[4]+','+row[6]+','+row[10] + '\n')
    print(f"Scraped data from {start_date} to {end_date}.")


def main():
    # scrape_dse('2021-01-01', '2021-01-31')
    # scrape_dse('2021-02-01', '2021-03-31')
    # scrape_dse('2021-04-01', '2021-06-30')
    # scrape_dse('2021-07-01', '2021-09-26')


if __name__ == '__main__':
    main()
