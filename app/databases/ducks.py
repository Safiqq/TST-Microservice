from typing import List
from models.ducks import Duck, DuckDB
from databases.connection import *

def create_duck(new_duck: DuckDB) -> int:
    sess.add(new_duck)
    sess.commit()
    new_duck_id = new_duck.id
    sess.close()
    return new_duck_id

def get_ducks() -> List[dict]:
    ducks = sess.query(DuckDB).all()
    ducks_dict = []
    for i in ducks:
        ducks_dict.append(i.to_dict())
    return ducks_dict

def get_duck_by_id(_id: int) -> dict:
    duck = sess.query(DuckDB).filter(DuckDB.id == _id).first()
    if duck:
        return duck.to_dict()
    return duck

def update_duck(_id: int, updated_duck: Duck) -> dict:
    duck = sess.query(DuckDB).filter(DuckDB.id == _id).first()
    
    duck.duck_name = updated_duck.duck_name
    duck.duck_type = updated_duck.duck_type
    duck.birthplace = updated_duck.birthplace
    duck.birthdate = updated_duck.birthdate
    duck.gender = updated_duck.gender
    duck.health_status = updated_duck.health_status
    duck.farm_id = updated_duck.farm_id

    sess.commit()
    duck_dict = duck.to_dict()
    sess.close()
    return duck_dict

def delete_duck(_id: int) -> int:
    duck = sess.query(DuckDB).filter(DuckDB.id == _id).first()
    sess.delete(duck)
    sess.commit()
    sess.close()
    return _id