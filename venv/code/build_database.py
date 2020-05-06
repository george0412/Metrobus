"""
Archivo que inicializa la base de datos
"""
import os
from config import db
from models import MetrobusDatos
from random import randint, seed
from datetime import datetime, timedelta
from geopy.geocoders import OpenCage
from opencage.geocoder import OpenCageGeocode

## Inicializar geopy
geolocators = OpenCage(api_key="fab369dfefcd443d918d5c91970e77d1")
geolocator = OpenCageGeocode("fab369dfefcd443d918d5c91970e77d1")

## Array de longitudes y latitudes del metrobus == 18 estaciones
lonLat = ["19.4930495,-99.1210605","19.44674162268097,-99.15331646617256","19.4236252,-99.1630861","19.4096721,-99.1680921","19.3858323,-99.175063","19.3700691,-99.1797636","19.364163,-99.1824701","19.354986,-99.1860674","19.3508802,-99.1863723","19.3424829,-99.1897309","19.3099899,-99.1845917","19.3143883,-99.1872434","19.3040286,-99.1860506","19.2973346,-99.1847422","19.2944284,-99.1839697","19.2903981,-99.1774466","19.282733,-99.1757382","19.280384,-99.1717675"]

## Datos para inicializar la base de datos
DATOS = []
for x in range(0, 50):
    update_time = datetime.now() - timedelta(hours=1)
    vehicle_id = randint(1,1500)
    lonLatId = randint(0,17)
    geographic_point = lonLat[lonLatId]
    lonLatArray = geographic_point.split(",")
    position_longitude = lonLatArray[0]
    position_latitude = lonLatArray[1]
    direccion = geolocator.reverse_geocode(position_longitude,position_latitude)
    alcaldia = direccion[0]['components']['county']
    vehicle_current_status = randint(1,2)
    position_speed = randint(0,16)
    item = {"update_time": update_time, "vehicle_id": vehicle_id, "position_latitude": position_latitude, "position_longitude": position_longitude, "geographic_point": geographic_point, "alcaldia": alcaldia, "position_speed": position_speed, "vehicle_current_status": vehicle_current_status}
    DATOS.append(item)

## Eliminar la base de datos si existe actualmente
if os.path.exists("metrobus.db"):
    os.remove("metrobus.db")

## Crear base de datos
db.create_all()

## Insertar datos a la base de datos
for metrobus in DATOS:
    m = MetrobusDatos(update_time=metrobus.get("update_time"), vehicle_id=metrobus.get("vehicle_id"), geographic_point=metrobus.get("geographic_point"),
                      position_longitude=metrobus.get("position_longitude"), position_latitude=metrobus.get("position_latitude"), vehicle_current_status=metrobus.get("vehicle_current_status"),
                      position_speed=metrobus.get("position_speed"), alcaldia=metrobus.get("alcaldia"))
    db.session.add(m)

db.session.commit()