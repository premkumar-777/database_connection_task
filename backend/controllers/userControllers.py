from models.usermodels import User
from utils.exceptions import user_not_found


def create_user(user, db):
    new_user = User(
        name=user.name,
        email=user.email,
        role=user.role
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"message": "User added", "user_id": new_user.id}


def get_all_users(db):
    return db.query(User).all()


def get_single_user(user_id, db):
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise user_not_found()

    return user


def delete_user_by_id(user_id, db):
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise user_not_found()

    db.delete(user)
    db.commit()

    return {"message": "User deleted", "user": user.name}


def update_user_by_id(user_id, updated_user, db):
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise user_not_found()

    user.name = updated_user.name
    user.email = updated_user.email
    user.role = updated_user.role

    db.commit()
    db.refresh(user)

    return {"message": "User updated"}
