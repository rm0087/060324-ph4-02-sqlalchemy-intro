# Flask RESTful Routing Practice

## Learning Goals (Part Two)

- Initializing and migrating databases with SQLAlchemy

- Searching for entries with GET requests

- Creating new data with POST requests

- Removing data with DELETE requests

- Updating with PATCH requests

## Getting Started

```bash
pipenv install
pipenv shell
cd server
```

## Migrating the Database

Write out your models similar to this:

```python
class Raccoon(db.Model):

    __tablename__ = 'raccoons_table'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
```

In the terminal run:

```bash
flask db init
flask db migrate -m "create raccoon table"
flask db upgrade
```

After the first time, if you ever make a change to a model you would only have to run:

```bash
flask db migrate -m "update raccoon table with more columns"
flask db upgrade
```

You may then do CRUD with those models using the `flask shell` command.

## Exercises - Part One

Create a new model of your choice with four attributes. Once you've created the model, migrate and upgrade the database.

In small groups create a new model of your choice with at least two attributes. Use `flask shell` to test the code below (replace `Item` with your model name and change attributes as necessary):

```python
item = Item(name="Bob")
db.session.add(item)
db.session.commit()
```

```python
itemsList = [ Item(name="Jim"), Item(name="Jane") ]
db.session.add_all(itemsList)
db.session.commit()
```

```python
Item.query.all()
```

```python
Item.query.where(Item.name == "Bob").first()
```

```python
item.name = "Bobbert"
db.session.add(item)
db.session.commit()
# this process will include more steps when we start routing later...
```

```python
db.session.delete(item)
db.session.commit()
```

## Exercises - Part Two

For your models add a `to_dict()` method that converts it from an instance into a dictionary.

Create these (restful) routes in order to perform basic CRUD for your model from the part one:

```
GET /items          respond with all items
GET /items/:id      respond with item by id
POST /items         create and respond with item
PATCH /items/:id    update and respond with item by id
DELETE /items/:id   delete item and respond with empty response
```

## RESTful Routes

!["restful routes chart"](assets/restful-routes.png)