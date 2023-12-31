# How to Use

1. `source venv/bin/activate`
2. `python3 main.py`


OR (docker it in **cloud**)


1. `docker build -t rtstmicroservice.azurecr.io/rtstmicroservice .`
2. `docker push rtstmicroservice.azurecr.io/rtstmicroservice`


OR (docker it **locally**)


1. `docker build -t tstimage .`
2. `docker run -d --name tstcontr -p 80:80 tstimage`

## Additional Commands

* Use `black app/*.py app/auth/*.py app/databases/*.py app/models/*.py app/routes/*.py app/schemas/*.py` to apply code formatter
* Use `pylint app/*.py app/auth/*.py app/databases/*.py app/models/*.py app/routes/*.py app/schemas/*.py` to rate the code lint

Create a table: `alembic revision -m "create {table_name} table`
Run migration: `alembic upgrade head`
Delete mgration: `alembic downgrade base`

1. python3 -m venv venv
2. source venv/bin/activate
3. pip install -r requirements.txt
4. python3 app/main.py