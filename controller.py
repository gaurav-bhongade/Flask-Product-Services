from models import Product
from config import app
from flask import request
import json

@app.route('',methods = [''])
def get_product():
    pass


# uri -- http://localhost:5000/api/v1/product  ---- GET
@app.route('/api/v1/product',methods = ['GET'])
def get_list_of_products():

    #fetch list of product fro db -- through sqlalchemy
    product_list = Product.query.all()

    # if no products in db return ---- simple message
    if not product_list:
        return json.dumps({"Error": "No Products..!"})

    final_product_list = []

    #iterate one by one and prepare dict
    for prod in product_list:
        prod_dict = {}
        prod_dict['PRODUCT ID'] = prod.id
        prod_dict['PRODUCT NAME'] = prod.name
        prod_dict['PRODUCT PRICE'] = prod.price
        prod_dict['PRODUCT QTY'] = prod.qty
        prod_dict['PRODUCT VENDOR'] = prod.vendor
        prod_dict['PRODUCT CATEGORY'] = prod.category

        #add that list every time in final product list
        final_product_list.append(prod_dict)

    if final_product_list:
        return json.dumps(final_product_list)


# uri -- http://localhost:5000/api/v1/product  ---- POST
@app.route('/api/v1/product',methods = ['POST'])
def save_product():
    print(request.__dict__)
    print(dir(request))
    return 'post method invoked'

@app.route('',methods = [''])
def add_new_product():
    pass

@app.route('',methods = [''])
def delete_product():
    pass

@app.route('',methods = [''])
def get_vendor_specific_product():
    pass

@app.route('',methods = [''])
def get_availibility_of_product():
    pass

@app.route('',methods = [''])
def get_product_price():
    pass

@app.route('',methods = [''])
def update_product():
    pass
