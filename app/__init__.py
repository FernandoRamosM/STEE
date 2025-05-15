from flask import Flask
from config import Config  # Importando la configuración

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)  # Aplicando configuración

    from app.rutas import bp
    app.register_blueprint(bp)

    return app