from config import db

# MODELS GO BELOW

class Candy(db.Model):

    #1. add tablename
    __tablename__ = 'candies_table'

    #2. start adding columns
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable = False)
    brand = db.Column(db.String)
    price = db.Column(db.Integer)

    # 3. make sure to import in app.py ==> "from models import Candy"

    # 4. flask db init (ONLY HAVE TO DO ONCE)

    # 5. flask db migrate -m "some message"

    # 6. flask db upgrade

    def to_dict(self): #transforms candy into dictionary
        return {"id": self.id,"name": self.name,"brand": self.brand,"price": self.price}
    
class Vegetable(db.Model):

    __tablename__ = 'vegetables_table'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable = False)
    is_tasty = db.Column(db.Boolean, default = True)

    def to_dict(self): #transforms vegetable into dictionary
        return {"id": self.id,"name": self.name,"is_tasty": self.is_tasty}