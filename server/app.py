#!/usr/bin/env python3

from flask import request
from config import app, db
from models import Candy, Vegetable

# from models import MODELS GO HERE


# ROUTES 

@app.get('/')
def index():
    return { "response": "hello world" }, 200

# CREATE

# CANDIES ########################################################################################################
@app.get('/candies') #READ ALL
def all_candies():
    # all_the_candies = Candy.query.all()
    # candy_dictionaries = []
    
    # for candy in all_the_candies:
    #     candy_dict = candy.to_dict()
    #     candy_dictionaries.append(candy_dict)
    #  candy_dictionaries = [candy.to_dict() for candy in all_the_candies]
    # return candy_dictionaries, 200
    return [candy.to_dict() for candy in Candy.query.all()], 200



@app.get('/candies/<int:id>') # READ BY ID
def candy_by_id(id):
    found_candy = Candy.query.where(Candy.id == id).first()
    
    if found_candy:
        return found_candy.to_dict(), 200
    else:
        return { 'error': 'Candy not found'}, 404
    
@app.post('/candies') #POST CANDIES
def make_new_amazing_candy():
    data = request.json

    try:  
        #1 make the instance
        new_candy = Candy(name=data['name'], brand=data['brand'], price=data['price'])
        # new_candy = Candy(**data)

        #add/commit the instance
        db.session.add(new_candy)
        db.session.commit()
    
        return new_candy.to_dict(), 201
    
    except:

        return {'error': "OH NOES"}, 400
    
@app.patch('/candies/<int:id>') # PATCH CANDIES
def update_candy(id):
    candy_to_update = Candy.query.where(Candy.id == id).first()
    
    if candy_to_update:
        
        data = request.json
        
        for key in data:
            setattr(candy_to_update, key, data[key])
        
        db.session.add(candy_to_update)
        db.session.commit()
        
        return candy_to_update.to_dict(), 202
    else:
        return {'error': 'Does not exist'}, 404
    
@app.delete('/candies/<int:id>') # DESTROY CANDIES
def delete_candy(id):
    candy_to_delete = Candy.query.where(Candy.id ==id).first()
    if candy_to_delete:
        db.session.delete(candy_to_delete)
        db.session.commit()

        return {}, 204
    else:
        return {'error': 'Not found'}, 404

# VEGETABLES ########################################################################################################
@app.get('/vegetables') # READ ALL
def all_vegetables():
    return [vegetable.to_dict() for vegetable in Vegetable.query.all()] , 200


@app.get('/vegetables/<int:id>') # READ BY ID
def vegetable_by_id(id):
    found_vegetable = Vegetable.query.where(Vegetable.id == id).first()
    
    if found_vegetable:
        return found_vegetable.to_dict(), 200
    else:
        return { 'error': 'Vegetable not found'}, 404

@app.post('/vegetables') #POST VEGETABLES
def make_new_amazing_vegetable():
    data = request.json

    try:  
        #1 make the instance
        new_vegetable = Vegetable(name=data['name'], is_tasty=data['is_tasty'])
        # new_candy = Candy(**data)

        #add/commit the instance
        db.session.add(new_vegetable)
        db.session.commit()
    
        return new_vegetable.to_dict(), 201
    
    except:

        return {'error': "OH NOES"}, 400

@app.delete('/vegetables/<int:id>') #DELETE VEGETABLES
def delete_vegetable(id):
    vegetable_to_delete = Vegetable.query.where(Vegetable.id ==id).first()
    if vegetable_to_delete:
        db.session.delete(vegetable_to_delete)
        db.session.commit()

        return {}, 204
    else:
        return {'error': 'Not found'}, 404
    





# APP RUN

if __name__ == '__main__':
    app.run(port=5555, debug=True)