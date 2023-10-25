import datetime as _dt
import sqlalchemy as _sql
import passlib.hash as _hash
import database as _database


class Users(_database.Base):
    __tablename__ = "users"
    uid = _sql.Column(_sql.Integer, primary_key=True, index=True)
    name = _sql.Column(_sql.String)
    email = _sql.Column(_sql.String, index=True)
    hashed_password = _sql.Column(_sql.Integer)

    def verify_password(self, password: str):
        return _hash.bcrypt.verify(password, self.hashed_password)
    

class Trips(_database.Base):
    __tablename__ = "trips"
    tripID = _sql.Column(_sql.String, unique=True, primary_key=True, index=True)
    uid = _sql.Column(_sql.Integer, _sql.ForeignKey("users.uid"), index=True)
    driverID = _sql.Column(_sql.Integer, unique=True, index=True)
    driverNO = _sql.Column(_sql.String, unique=True, index=True)
    # deviceID = _sql.Column(_sql.Integer, _sql.ForeignKey("devices.deviceID"), unique=True, index=True)
    srcLoc = _sql.Column(_sql.String)
    src = _sql.Column(_sql.String)
    destLoc = _sql.Column(_sql.String)
    dest = _sql.Column(_sql.String)
    # eta = _sql.Column(_sql.Time)
    # cp1 = _sql.Column(_sql.Boolean, default=" ")
    # cp2 = _sql.Column(_sql.Boolean, default=" ")
    # cp3 = _sql.Column(_sql.Boolean, default=" ")

class Warehouses(_database.Base):
    __tablename__ = "wares"
    whID = _sql.Column(_sql.Integer, primary_key=True, index=True)
    uid = _sql.Column(_sql.Integer, _sql.ForeignKey("users.uid"), index=True)
    ownerID = _sql.Column(_sql.Integer, index=True)
    ownerNO = _sql.Column(_sql.String, index=True)
    # deviceID = _sql.Column(_sql.Integer, _sql.ForeignKey("devices.deviceID"), unique=True, index=True)
    whLoc = _sql.Column(_sql.String)

class Assets(_database.Base):
    __tablename__ = "assets"
    assetID = _sql.Column(_sql.Integer, primary_key=True, index=True)
    whID = _sql.Column(_sql.Integer, _sql.ForeignKey("wares.whID"), index=True)
    tripID = _sql.Column(_sql.Integer, _sql.ForeignKey("trips.tripID"), index=True)
    assetName = _sql.Column(_sql.String)
    assetType = _sql.Column(_sql.String)
    src = _sql.Column(_sql.String)

class Devices(_database.Base):
    __tablename__ = "devices"
    deviceID = _sql.Column(_sql.Integer, primary_key=True, index=True)
    whID = _sql.Column(_sql.Integer, _sql.ForeignKey("wares.whID"), index=True)
    tripID = _sql.Column(_sql.Integer, _sql.ForeignKey("trips.tripID"), index=True)
    deviceName = _sql.Column(_sql.String)
    status = _sql.Column(_sql.String)

class Sensors(_database.Base):
    __tablename__ = "sensors"
    entryID = _sql.Column(_sql.Integer, unique=True, primary_key=True, index=True)
    # timestamp = _sql.Column(_sql.Time)
    deviceID = _sql.Column(_sql.Integer, _sql.ForeignKey("devices.deviceID"))
    temperature = _sql.Column(_sql.Float)
    humidity = _sql.Column(_sql.Float)
    pressure = _sql.Column(_sql.Float)
    light = _sql.Column(_sql.Float)
    shock = _sql.Column(_sql.Float)
    latitude = _sql.Column(_sql.String)
    longitude = _sql.Column(_sql.String)

class Alarms(_database.Base):
    __tablename__ = "alarms"
    alarmID = _sql.Column(_sql.Integer, unique=True, primary_key=True, index=True)
    uid = _sql.Column(_sql.Integer, _sql.ForeignKey("users.uid"), index=True)
    deviceID = _sql.Column(_sql.Integer, _sql.ForeignKey("devices.deviceID"),  index=True)
    entryID = _sql.Column(_sql.Integer, _sql.ForeignKey("sensors.entryID"),  index=True)
    desc = _sql.Column(_sql.String)