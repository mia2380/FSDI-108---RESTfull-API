from flask import Flask
import json
from config import me
from mock_data import catalog

app = Flask("server")


@app.get("/")
def home():
    return "Hello from Flask"


@app.get("/test")
def test():
    return "This is another endpoint"


@app.get("/about")
def about():
    return "Brenda Allemand"


##################################################################
####################  CATALOG API ################################
##################################################################

@app.get("/api/version")
def version():
    version = {
        "v": "v1.0.4",
        "name": "zombie rabbit",
    }
    # parse a dictionary into json
    return json.dumps(version)


@app.get("/api/about")
def get_about():
    return json.dumps(me)

# get /api/about
# return me as json


@app.get("/api/catalog")
def api_catalog():
    return json.dumps(catalog)


@app.get("/api/test/count")
def num_of_products():
    return len(catalog)


@app.get("/api/catalog/<category>")
def by_category(category):
    results = []
    category = category.lower()
    for product in catalog:
        if product["category"].lower() == category.lower():
            results.append(product)
    return json.dumps(results)


@app.get("/api/catalog/search/<text>")
def search_by_text(text):
    text = text.lower()
    results = []

    for product in catalog:
        if text in product["title"].lower():
            results.append(product)
    return json.dumps(results)


@app.get("/api/categories")
def get_categories():
    results = []
    for product in catalog:
        cat = product["category"]
        if cat not in results:
            results.append(cat)

    return json.dumps(results)


@app.get("/api/test/value")
def total_value():
    total = 0
    for product in catalog:
        # total += total + product["price"]
        total = total + product["price"]

    return json.dumps(total)


@app.get("/api/product/<_id>")
def search_by_id(_id):
    for product in catalog:
        if product["_id"] == _id:
            return json.dumps(product)

    return "Error: Product not found"


app.run(debug=True)
