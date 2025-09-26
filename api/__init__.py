from flask import Flask
from .routes import register_routes

def create_api(app: Flask):
    register_routes(app)
