from fastapi import FastAPI

from services import collect_product_data, collect_advert_data

PRODUCT_URL_TEMPLATE = 'https://bina.az/items/{id}'

app = FastAPI()


@app.get("/product/{product_id}")
async def get_product_data(product_id: int):
    product_url = PRODUCT_URL_TEMPLATE.format(id=product_id)
    product_data = collect_product_data(product_url)
    return {"url": product_url, 'product': product_data}


@app.get("/advert/{product_id}")
async def get_advert_data(product_id: int):
    product_url = PRODUCT_URL_TEMPLATE.format(id=product_id)
    advert_data = collect_advert_data(product_url)
    return {"url": product_url, 'advert': advert_data}
