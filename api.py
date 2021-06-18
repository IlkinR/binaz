from fastapi import FastAPI

from services import collect_product_data

PRODUCT_URL_TEMPLATE = 'https://bina.az/items/{id}'

app = FastAPI()


@app.get("/product/{product_id}")
async def root(product_id: int):
    product_url = PRODUCT_URL_TEMPLATE.format(id=product_id)
    product = collect_product_data(product_url)
    return {"url": product_url, 'product': product}
