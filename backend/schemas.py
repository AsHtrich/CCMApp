import datetime as _dt
from typing import Optional
import pydantic as _pyd

class _UserBase(_pyd.BaseModel):
    name: str
    email: str

    class Config:
        from_attributes =True
        

class UserCreate(_UserBase):
    hashed_password: str
    

    class Config:
        from_attributes =True
        

class User(_UserBase):
    uid: int
    

    class Config:
        from_attributes =True
        

# ---------------------------------------------

class _TripsBase(_pyd.BaseModel):
    uid: int
    driverNO: str
    # eta: _dt.datetime
    # cp1: bool = False
    # cp2: bool = False
    # cp3: bool = False
    src: str
    srcLoc: str
    destLoc: str
    dest: str
    tripID: int
    driverID: int

class TripCreate(_TripsBase):
    pass

class Trips(_TripsBase):
    pass
    

    class Config:
        from_attributes =True
        

    
# ---------------------------------------------

class _WhBase(_pyd.BaseModel):
    uid: int
    ownerNO: str
    whLoc: str
    whID: int
    ownerID: int

class WareCreate(_WhBase):
    pass
  
class Warehouses(_WhBase):
    pass

    class Config:
        from_attributes =True
        

# ---------------------------------------------

class _AssetBase(_pyd.BaseModel):
    assetName: str
    assetType: str
    src: str
    assetID: int
    whID: int
    tripID: int

class AssetCreate(_AssetBase):
    pass

class Assets(_AssetBase):
    pass

    class Config:
        from_attributes =True
        


# ---------------------------------------------

class _DeviceBase(_pyd.BaseModel):
    status: str
    deviceName: str
    deviceID: int
    whID: int
    tripID: int

class DeviceCreate(_DeviceBase):
    pass

class Devices(_DeviceBase):
    pass
    

    class Config:
        from_attributes =True
        


# ---------------------------------------------

class _SensorBase(_pyd.BaseModel):
    temperature: float
    pressure: float
    humidity: float
    light: float
    shock: float
    latitude: str
    longitude: str
    entryID: int
    timestamp: _dt.datetime
    deviceID: int

class SensorCreate(_SensorBase):
    pass

class Sensors(_SensorBase):
    pass

    class Config:
        from_attributes =True
        

# ---------------------------------------------

class _AlarmBase(_pyd.BaseModel):
    desc: str
    uid: int
    deviceID: int
    entryID: int
    alarmID: int
    timestamp : _dt.datetime

class AlarmCreate(_AlarmBase):
    pass

class Alarms(_AlarmBase):
    
    pass
    
    class Config:
        from_attributes =True
        


# ---------------------------------------------

