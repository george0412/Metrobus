"""
Módulo principal
"""
from flask import render_template
import config
import schedule, time, threading
from datetime import timedelta, datetime

## Trae la instancia de la aplicacion creada en config.py
connex_app = config.connex_app

## Trae la configuración de los endpoints
connex_app.add_api("swagger.yml")

## Crea la ruta URL de la aplicación
@connex_app.route("/")
def home():
    return render_template("home.html")

if __name__ == "__main__":
    connex_app.run(debug=True)