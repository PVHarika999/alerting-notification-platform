from .admin_routes import admin_bp
from .user_routes import user_bp  
from .analytics_routes import analytics_bp

def register_routes(app):
    app.register_blueprint(admin_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(analytics_bp)
