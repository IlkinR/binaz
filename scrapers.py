from datetime import date
import requests
from bs4 import BeautifulSoup


def get_soup(url):
    response = requests.get(url).content
    soup = BeautifulSoup(response, 'lxml')
    return soup


class ProductScraper:
    def __init__(self, product_url):
        self.url = product_url
        self.soup = get_soup(self.url)

    def get_price(self):
        price_tag = self.soup.find('span', class_='price-val')
        return price_tag.text

    def get_ownership(self):
        owner_tag = self.soup.select('div.name > span')
        return [tag.text for tag in owner_tag]

    def get_title(self):
        title_tag = self.soup.select('div.services-container > h1')[0]
        return title_tag.text

    def get_table_props(self):
        prop_tags = self.soup.select('table.parameters > tr')
        props = {}

        for tag in prop_tags:
            prop_data = [td.text for td in tag.find_all('td')]
            prop_label, prop_value = prop_data
            props[prop_label] = prop_value

        return props

    def get_locations(self):
        location_tags = self.soup.select('ul.locations > li')
        return [loc_tag.text for loc_tag in location_tags]


class AdvertScraper:
    @classmethod
    def _parse_advert_tag(cls, advert_tag):
        ad_data = advert_tag.text.split(':')
        ad_label = ad_data[0].strip()
        ad_value = ' '.join(ad_data[1:])
        return ad_label, ad_value

    def __init__(self, url):
        self.soup = get_soup(url)
        self.advert_tags = self.soup.select('div.item_info > p')

    def scrape_data(self):
        dataset = {}

        for advert_tag in self.advert_tags:
            label, value = self._parse_advert_tag(advert_tag)
            dataset[label] = value
            dataset['today'] = date.today().strftime("%d/%m/%Y")

        return dataset
