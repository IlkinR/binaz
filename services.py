from scrapers import AdvertScraper, ProductScraper


def collect_product_data(product_url):
    advert_scraper = AdvertScraper(product_url)
    product_scraper = ProductScraper(product_url)

    product_dataset = product_scraper.get_table_props()
    product_dataset['title'] = product_scraper.get_title()
    product_dataset['price'] = product_scraper.get_price()
    product_dataset['ownership'] = product_scraper.get_ownership()
    product_dataset['location'] = product_scraper.get_locations()

    product_dataset['advert'] = advert_scraper.scrape_data()

    return product_dataset
