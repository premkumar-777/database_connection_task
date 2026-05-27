from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from controllers.userControllers import (
    create_user,
    delete_user_by_id,
    get_all_users,
    get_single_user,
    update_user_by_id,
)
from db.database import get_db
from schemas.user_schema import UserCreate
from utils.routes import USER_ROUTES
from utils.status_codes import CREATED, SUCCESS

router = APIRouter(prefix=USER_ROUTES)


@router.get("/", status_code=SUCCESS)
def read_users(db: Session = Depends(get_db)):
    return get_all_users(db)


@router.get("/{user_id}", status_code=SUCCESS)
def read_user(user_id: int, db: Session = Depends(get_db)):
    return get_single_user(user_id, db)


@router.post("/", status_code=CREATED)
def add_user(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(user, db)


@router.put("/{user_id}", status_code=SUCCESS)
def update(user_id: int, user: UserCreate, db: Session = Depends(get_db)):
    return update_user_by_id(user_id, user, db)


@router.delete("/{user_id}", status_code=SUCCESS)
def delete(user_id: int, db: Session = Depends(get_db)):
    return delete_user_by_id(user_id, db)
