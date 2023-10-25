import fastapi as _fastapi
import fastapi.security as _security
import datetime as _dt
import sqlalchemy.orm as _orm
import passlib.hash as _hash
import database as _database, models as _models, schemas as _schemas
import jwt as _jwt

oauth2schema = _security.OAuth2PasswordBearer(tokenUrl="/api/token")
JWT_SECRET = "myjwtsecret"

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


async def create_trips(trip: _schemas.Trips, user: _schemas.User, db: _orm.Session):
    existing_trip = db.query(_models.Trips).filter(_models.Trips.tripID == trip.tripID).first()
    if existing_trip:
        raise _fastapi.HTTPException(status_code=400, detail="Duplicate tripID")
    
    existing_driver = db.query(_models.Trips).filter(_models.Trips.driverID == trip.driverID).first()
    if existing_driver:
        raise _fastapi.HTTPException(status_code=400, detail="Driver assigned to another trip!")
    
    trip_obj = _models.Trips(
        tripID=trip.tripID, driverID=trip.driverID, driverNO=trip.driverNO, src=trip.src, srcLoc=trip.srcLoc, dest=trip.dest, destLoc=trip.destLoc, uid=user.uid
    )
    db.add(trip_obj)
    db.commit()
    db.refresh(trip_obj)
    return trip_obj

async def create_wares(ware: _schemas.Warehouses, user: _schemas.User, db: _orm.Session):
    existing_ware = db.query(_models.Warehouses).filter(_models.Warehouses.whID == ware.whID).first()
    if existing_ware:
        raise _fastapi.HTTPException(status_code=400, detail="Duplicate whID")
    
    
    wh_obj = _models.Warehouses(
        whID=ware.whID, ownerID=ware.ownerID, ownerNO=ware.ownerNO, whLoc=ware.whLoc, uid=user.uid
    )
    db.add(wh_obj)
    db.commit()
    db.refresh(wh_obj)
    return wh_obj

async def create_devices(trip: _schemas.Trips, ware: _schemas.Warehouses, device: _schemas.Devices, user: _schemas.User, db: _orm.Session):
    
    existing_device = db.query(_models.Devices).filter(_models.Devices.deviceID == device.deviceID).first()
    if existing_device:
        raise _fastapi.HTTPException(status_code=400, detail="Duplicate deviceID")
    
    existing_trip = db.query(_models.Devices).filter(_models.Devices.tripID == device.tripID).first() 
    if existing_trip:
        raise _fastapi.HTTPException(status_code=400, detail="tripID already assigned to another device")
    
    trip_obj = db.query(_models.Trips).filter(_models.Trips.tripID == trip.tripID).first() 
    if not trip_obj:
        raise _fastapi.HTTPException(status_code=400, detail="Invalid tripID")
    
    ware_obj = db.query(_models.Warehouses).filter(_models.Warehouses.whID == ware.whID).first() 
    if not ware_obj:
        raise _fastapi.HTTPException(status_code=400, detail="Invalid whID")
    
    existing_ware = db.query(_models.Devices).filter(_models.Devices.whID == device.whID).first() 
    if existing_ware:
        raise _fastapi.HTTPException(status_code=400, detail="whID already assigned to another device")



    device_obj = _models.Devices(
        deviceID=device.deviceID, status=device.status, deviceName=device.deviceName, whID=ware.whID, tripID=trip.tripID
    )
    db.add(device_obj)
    db.commit()
    db.refresh(device_obj)
    return device_obj

async def create_assets(trip: _schemas.Trips, ware: _schemas.Warehouses, asset: _schemas.Assets, user: _schemas.User, db: _orm.Session):
    
    existing_asset = db.query(_models.Assets).filter(_models.Assets.assetID == asset.assetID).first()
    if existing_asset:
        raise _fastapi.HTTPException(status_code=400, detail="Duplicate assetID")
    
    existing_trip = db.query(_models.Assets).filter(_models.Assets.tripID == asset.tripID).first() 
    if existing_trip:
        raise _fastapi.HTTPException(status_code=400, detail="tripID already assigned to another asset")
    
    trip_obj = db.query(_models.Trips).filter(_models.Trips.tripID == trip.tripID).first() 
    if not trip_obj:
        raise _fastapi.HTTPException(status_code=400, detail="Invalid tripID")
    
    ware_obj = db.query(_models.Warehouses).filter(_models.Warehouses.whID == ware.whID).first() 
    if not ware_obj:
        raise _fastapi.HTTPException(status_code=400, detail="Invalid whID")
    
    existing_ware = db.query(_models.Assets).filter(_models.Assets.whID == asset.whID).first() 
    if existing_ware:
        raise _fastapi.HTTPException(status_code=400, detail="whID already assigned to another asset")



    asset_obj = _models.Assets(
        assetID=asset.assetID, src=asset.src, assetName=asset.assetName, assetType=asset.assetType, whID=ware.whID, tripID=trip.tripID
    )
    db.add(asset_obj)
    db.commit()
    db.refresh(asset_obj)
    return asset_obj


async def create_sensors(device: _schemas.Devices, sens: _schemas.Sensors, user: _schemas.User, db: _orm.Session):
    existing_entry = db.query(_models.Sensors).filter(_models.Sensors.entryID == sens.entryID).first()
    if existing_entry:
        raise _fastapi.HTTPException(status_code=400, detail="Duplicate entryID")
    
    device_obj = db.query(_models.Devices).filter(_models.Devices.deviceID == device.deviceID).first() 
    if not device_obj:
        raise _fastapi.HTTPException(status_code=400, detail="Invalid deviceID")
    
    sens_obj = _models.Sensors(
        entryID=sens.entryID, temperature=sens.temperature, pressure=sens.pressure, humidity=sens.humidity, light=sens.light, shock=sens.shock, latitude=sens.latitude, longitude=sens.longitude, deviceID=sens.deviceID
    )
    db.add(sens_obj)
    db.commit()
    db.refresh(sens_obj)
    return sens_obj

async def create_alarms(alarm: _schemas.Alarms, sens: _schemas.Sensors, device:_schemas.Devices, user: _schemas.User, db: _orm.Session):
    
    existing_alarm = db.query(_models.Alarms).filter(_models.Alarms.alarmID == alarm.alarmID).first()
    if existing_alarm:
        raise _fastapi.HTTPException(status_code=400, detail="Duplicate alarmID")
    
    sensor_obj = db.query(_models.Sensors).filter(_models.Sensors.entryID == sens.entryID).first() 
    if not sensor_obj:
        raise _fastapi.HTTPException(status_code=400, detail="Invalid entryID")
    
    device_obj = db.query(_models.Devices).filter(_models.Devices.deviceID == device.deviceID).first() 
    if not device_obj:
        raise _fastapi.HTTPException(status_code=400, detail="Invalid deviceID")
    alarm_obj = _models.Alarms(
        entryID=alarm.entryID, alarmID=alarm.alarmID, desc=alarm.desc, deviceID=alarm.deviceID, uid=alarm.uid
    )
    db.add(alarm_obj)
    db.commit()
    db.refresh(alarm_obj)
    return alarm_obj