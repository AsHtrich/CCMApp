import fastapi as _fastapi
import fastapi.security as _security
import datetime as _dt
import sqlalchemy.orm as _orm
import passlib.hash as _hash
import database as _database, models as _models, schemas as _schemas
import random
import string
import jwt as _jwt

oauth2schema = _security.OAuth2PasswordBearer(tokenUrl="/api/token")
JWT_SECRET = "myjwtsecret"

def generate_random_id():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=3))

def create_database():
    return _database.Base.metadata.create_all(bind=_database.engine)


def get_db():
    db = _database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

async def get_user_by_email(email: str, db: _orm.Session):
    return db.query(_models.Users).filter(_models.Users.email == email).first()


async def create_user(user: _schemas.UserCreate, db: _orm.Session):
    user_obj = _models.Users(
        email=user.email, hashed_password=_hash.bcrypt.hash(user.hashed_password), name=user.name
    )
    db.add(user_obj)
    db.commit()
    db.refresh(user_obj)
    return user_obj

async def authUser(email:str, password: str, db: _orm.Session):
    user = await get_user_by_email(db=db, email=email)

    if not user:
        return False
    if not user.verify_password(password):
        return False
    return user

async def create_token(user: _models.Users):
    user_obj = _schemas.User.model_validate(user)

    token = _jwt.encode(user_obj.model_dump(), JWT_SECRET)

    return dict(access_token = token, token_type="bearer")

async def get_current_user(db: _orm.Session= _fastapi.Depends(get_db), token: str= _fastapi.Depends(oauth2schema)):
    try:
        payload = _jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
        user= db.query(_models.Users).get(payload["uid"])
    except:
        raise _fastapi.HTTPException(status_code=401, detail="Invalid Email or Password")
    
    return _schemas.User.model_validate(user)
    