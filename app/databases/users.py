from typing import List
from models.users import User, UserDB
from databases.connection import *

def create_user(new_user: UserDB) -> int:
    sess.add(new_user)
    sess.commit()
    new_user_id = new_user.id
    sess.close()
    return new_user_id

def get_users() -> List[dict]:
    users = sess.query(UserDB).all()
    users_dict = []
    for i in users:
        users_dict.append(i.to_dict())
    return users_dict

def get_user_by_username(username: str) -> dict:
    user = sess.query(UserDB).filter(UserDB.username == username).first()
    if user:
        return user.to_dict()
    return user

def update_user(_id: int, updated_user: User) -> dict:
    user = sess.query(UserDB).filter(UserDB.id == _id).first()
    
    user.user_name = updated_user.user_name
    user.user_location = updated_user.user_location
    user.number_of_barns = updated_user.number_of_barns
    user.total_capacity = updated_user.total_capacity
    user.owner_name = updated_user.owner_name
    user.phone_number = updated_user.phone_number

    sess.commit()
    user_dict = user.to_dict()
    sess.close()
    return user_dict

def delete_user(_id: int) -> int:
    user = sess.query(UserDB).filter(UserDB.id == _id).first()
    sess.delete(user)
    sess.commit()
    sess.close()
    return _id