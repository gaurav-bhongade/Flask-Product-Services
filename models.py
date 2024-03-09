from config import db

class Product(db.Model):
    id = db.Column('prod_id',db.Integer,primary_key=True)
    name = db.Column('prod_name',db.String(30))
    category = db.Column('prod_category',db.String(30))
    price = db.Column('prod_price',db.Float())
    vendor = db.Column('prod_vendor',db.String(30))
    qty = db.Column('prod_qty',db.Integer)

print('Product is created......')
db.create_all()


