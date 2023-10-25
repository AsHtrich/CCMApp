
import fastapi as _fastapi
import fastapi.security as _security

import sqlalchemy.orm as _orm

import services as _services, schemas as _schemas

app = _fastapi.FastAPI()


@app.post("/api/users")
async def create_user(
    user: _schemas.UserCreate, db: _orm.Session = _fastapi.Depends(_services.get_db)
):
    db_user = await _services.get_user_by_email(user.email, db)
    if db_user:
        raise _fastapi.HTTPException(status_code=400, detail="Email already in use")

    user = await _services.create_user(user, db)

    return await _services.create_token(user)

@app.post("/api/token")
async def generate_token(form_data: _security.OAuth2PasswordRequestForm = _fastapi.Depends(), db: _orm.Session = _fastapi.Depends(_services.get_db)):
    user = await _services.authUser(form_data.username, form_data.password, db)
    if not user:
        raise _fastapi.HTTPException(status_code=401, detail="Invalid Credentials")
    return await _services.create_token(user)

@app.get("/api/users/me", response_model=_schemas.User)
async def get_user(user: _schemas.User = _fastapi.Depends(_services.get_current_user)):
    return user 

@app.post("/api/trips", response_model=_schemas.Trips)
async def create_trips(user: _schemas.User = _fastapi.Depends(_services.get_current_user), db: _orm.Session = _fastapi.Depends(_services.get_db),):
    return await _services.create_trips(user=user, db=db)

@app.post("/api/wares", response_model=_schemas.Warehouses)
async def create_wares( ware: _schemas.Warehouses, user: _schemas.User = _fastapi.Depends(_services.get_current_user), db: _orm.Session = _fastapi.Depends(_services.get_db),):
    return await _services.create_wares(user=user, db=db, ware=ware)

@app.post("/api/devices", response_model=_schemas.Devices)
async def create_devices( device: _schemas.Devices, trip: _schemas.Trips,ware: _schemas.Warehouses, user: _schemas.User = _fastapi.Depends(_services.get_current_user), db: _orm.Session = _fastapi.Depends(_services.get_db),):
    return await _services.create_devices(user=user, db=db, device=device, trip=trip, ware=ware)

@app.post("/api/assets", response_model=_schemas.Assets)
async def create_assets( asset: _schemas.Assets, trip: _schemas.Trips, ware: _schemas.Warehouses, user: _schemas.User = _fastapi.Depends(_services.get_current_user), db: _orm.Session = _fastapi.Depends(_services.get_db),):
    return await _services.create_assets(user=user, db=db, asset=asset, trip=trip, ware=ware)

@app.post("/api/sensors", response_model=_schemas.Sensors)
async def create_sensors( device: _schemas.Devices, sens: _schemas.Sensors, user: _schemas.User = _fastapi.Depends(_services.get_current_user), db: _orm.Session = _fastapi.Depends(_services.get_db),):
    return await _services.create_sensors(user=user, db=db, device=device, sens=sens)
@app.post("/api/alarms", response_model=_schemas.Alarms)
async def create_alarms( device: _schemas.Devices,sens: _schemas.Sensors, alarm: _schemas.Alarms, user: _schemas.User = _fastapi.Depends(_services.get_current_user), db: _orm.Session = _fastapi.Depends(_services.get_db),):
    return await _services.create_alarms(user=user, db=db, device=device, sens=sens, alarm=alarm)