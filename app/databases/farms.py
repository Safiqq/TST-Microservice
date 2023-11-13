from typing import List
from models.farms import Farm, FarmDB
from databases.connection import *

def create_farm(new_farm: FarmDB) -> int:
    sess.add(new_farm)
    sess.commit()
    new_farm_id = new_farm.id
    sess.close()
    return new_farm_id

def get_farms() -> List[dict]:
    farms = sess.query(FarmDB).all()
    farms_dict = []
    for i in farms:
        farms_dict.append(i.to_dict())
    return farms_dict

def get_farm_by_id(_id: int) -> dict:
    farm = sess.query(FarmDB).filter(FarmDB.id == _id).first()
    if farm:
        return farm.to_dict()
    return farm

def update_farm(_id: int, updated_farm: Farm) -> dict:
    farm = sess.query(FarmDB).filter(FarmDB.id == _id).first()
    
    farm.farm_name = updated_farm.farm_name
    farm.farm_location = updated_farm.farm_location
    farm.number_of_barns = updated_farm.number_of_barns
    farm.total_capacity = updated_farm.total_capacity
    farm.owner_name = updated_farm.owner_name
    farm.phone_number = updated_farm.phone_number

    sess.commit()
    farm_dict = farm.to_dict()
    sess.close()
    return farm_dict

def delete_farm(_id: int) -> int:
    farm = sess.query(FarmDB).filter(FarmDB.id == _id).first()
    sess.delete(farm)
    sess.commit()
    sess.close()
    return _id