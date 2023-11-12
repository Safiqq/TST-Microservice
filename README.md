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

* Use `black app/*.py app/models/*.py app/routes/*.py` to apply code formatter
* Use `pylint app/*.py app/models/*.py app/routes/*.py` to rate the code lint

Create a table: `alembic revision -m "create {table_name} table`
Run migration: `alembic upgrade head`
Delete mgration: `alembic downgrade base`