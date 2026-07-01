from sqlalchemy.orm import Session

from backend.models.user import User
from backend.schemas.user import UserCreate
from backend.utils.security import hash_password


def create_user(db: Session, user: UserCreate):
    db_user = User(
        full_name=user.full_name,
        email=user.email,
        hashed_password=hash_password(user.password)
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user