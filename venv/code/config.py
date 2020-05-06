import os
import connexion
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

basedir = os.path.abspath(os.path.dirname(__file__))

## Instancia de la conexión
connex_app = connexion.App(__name__, specification_dir=basedir)

## Instancia Flask app
app = connex_app.app

# Establece la URL de SQLite para SQLAlchemy
sqlite_url = "sqlite:///" + os.path.join(basedir, "metrobus.db")

## Configuración de SQLAlchemy
app.config["SQLALCHEMY_ECHO"] = True
app.config["SQLALCHEMY_DATABASE_URI"] = sqlite_url
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

## Crea la instancia de SQLAlchemy en variable db
db = SQLAlchemy(app)

## Inicializa Marshmallow
ma = Marshmallow (app)