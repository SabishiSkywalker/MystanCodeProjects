"""
File: webcrawler.py
Name: Jason Lee
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male Number: 10900879
Female Number: 7946050
---------------------------
2000s
Male Number: 12977993
Female Number: 9209211
---------------------------
1990s
Male Number: 14146310
Female Number: 10644506
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')

        # ----- Write your code below this line ----- #

        # Find the table with the name data
        table = soup.find('table', {'class': 't-stripe'})

        # Initialize counters
        male_count = 0
        female_count = 0

        # Find the tbody element within the table
        tag = table.find('tbody')

        # Iterate over the rows in tbody
        for row in tag.find_all('tr'):
            cells = row.find_all('td')

            # Ensure the row has the expected number of cells
            if len(cells) >= 5:
                # Extract data for male and female names
                male_rank = cells[0].text.strip()

                male_number = cells[2].text.strip().replace(',', '')

                female_number = cells[4].text.strip().replace(',', '')

            # Check if the rank is within the top 200 and update the counts
                if int(male_rank) <= 200:
                    male_count += int(male_number)
                if int(male_rank) <= 200:
                    female_count += int(female_number)

        print('Male Number:', male_count)
        print('Female Number:', female_count)


if __name__ == '__main__':
    main()
