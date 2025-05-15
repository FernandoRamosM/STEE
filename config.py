import os

class Config:
    SECRET_KEY    = os.getenv("SECRET_KEY", "R@mos218::")
    BASE_DIR      = os.path.abspath(os.path.dirname(__file__))
    DATABASE_PATH = os.path.join(BASE_DIR, 'app/models/db/STRC4.db')
    #   ============================================================
    #   ----------------------- RUTAS ------------------------------
    #   ============================================================
    RT_LOGIN       = "STRC4.html"
    RT_HOME        = "US/home.html"
    RT_INTEGRANTES = "US/integrantes.html"