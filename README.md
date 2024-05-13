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
flask db migrate
flask db upgrade
```

After the first time, if you ever make a change to a model you would only have to run:

```bash
flask db migrate
flask db upgrade
```

## RESTful Routes

!["restful routes chart"](assets/restful-routes.png)