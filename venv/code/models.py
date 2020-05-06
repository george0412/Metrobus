from datetime import datetime
from config import db, ma
from marshmallow import Schema
from marshmallow_sqlalchemy import ModelSchema

class MetrobusDatos(db.Model):
    __tablename__ = "metrobus"
    metrobus_id = db.Column(db.Integer, primary_key=True)
    update_time = db.Column(db.DateTime)
    vehicle_id = db.Column(db.Integer)
    geographic_point = db.Column(db.String(50))
    position_longitude = db.Column(db.String(32))
    position_latitude = db.Column(db.String(32))
    alcaldia = db.Column(db.String(32))
    vehicle_current_status = db.Column(db.Integer)
    position_speed = db.Column(db.String(5))

class MetrobusDatosSchema(ModelSchema):
    class Meta:
        model = MetrobusDatos
        sqla_session = db.session

class MetrobusDatosSchemaAlcaldia(ModelSchema):
    class Meta:
        model = MetrobusDatos
        sqla_session = db.session
        listFields = ['alcaldia']