"""
Archivo para realizar todas las acciones REST
"""
from flask import  make_response, abort
from config import db
from models import MetrobusDatos, MetrobusDatosSchema, MetrobusDatosSchemaAlcaldia

## Muestra todas las unidades
def read_all():
    ## Crea la lista de datos
    metrobus = MetrobusDatos.query.order_by(MetrobusDatos.update_time).all()
    metrobus_schema = MetrobusDatosSchema(many=True)
    data = metrobus_schema.dump(metrobus)
    return data

## Muestra las unidades disponibles
def read_available(vehicle_current_status):
    ## Busca unidades disponibles
    metrobus = MetrobusDatos.query.filter(MetrobusDatos.vehicle_current_status == vehicle_current_status).order_by(MetrobusDatos.update_time).all()

    if metrobus is not None:
        metrobus_schema = MetrobusDatosSchema()
        data = metrobus_schema.dump(metrobus, many=True)
        return data
    else:
        abort(
            404,
            "El estatus de vehículo ingresado, no existe"
        )

## Muestra el historial de una unidad dado su id
def read_id(vehicle_id):
    ## Busca unidades disponibles
    metrobus = MetrobusDatos.query.filter(MetrobusDatos.vehicle_id == vehicle_id).order_by(MetrobusDatos.update_time).all()

    if metrobus is not None:
        metrobus_schema = MetrobusDatosSchema()
        data = metrobus_schema.dump(metrobus, many=True)
        return data
    else:
        abort(
            404,
            "El vehículo ingresado, no existe"
        )

## Muestra alcaldías disponibles
def read_alcaldia():
    ## Busca unidades disponibles
    metrobus = MetrobusDatos.query.group_by(MetrobusDatos.alcaldia).order_by(MetrobusDatos.alcaldia).all()
    listFields = ['alcaldia']
    if metrobus is not None:
        metrobus_schema = MetrobusDatosSchemaAlcaldia(only=listFields)
        data = metrobus_schema.dump(metrobus, many=True)
        return data
    else:
        abort(
            404,
            "El vehículo ingresado, no existe"
        )

## Muestra vehículos en alcaldías disponibles
def read_vehiculoAlcaldia():
    ## Busca unidades disponibles
    metrobus = MetrobusDatos.query.group_by(MetrobusDatos.alcaldia, MetrobusDatos.vehicle_id).order_by(MetrobusDatos.alcaldia).all()
    listFields = ['alcaldia','vehicle_id']
    if metrobus is not None:
        metrobus_schema = MetrobusDatosSchemaAlcaldia(only=listFields)
        data = metrobus_schema.dump(metrobus, many=True)
        return data
    else:
        abort(
            404,
            "El vehículo ingresado, no existe"
        )