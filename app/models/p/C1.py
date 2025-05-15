import sqlite3
from config import Config
"""
NOMBRE PROCESO      :   C1.py
DESCRIPCION PROCESO :   Estable conexion a la base de datos
FECHA CREACION      :   2025-04-01
------------------------------------------------------------------------------------------------
FECHA       DESCRIPCION MODIFICACION                                    MODIFICADO POR
------------------------------------------------------------------------------------------------
"""

class conn():
    def __init__(self, name = Config.DATABASE_PATH):
        self.name = name
        self.conn = None
        self.curr = None

    def open(self):
        try:
            self.conn = sqlite3.connect(self.name)
            self.curr = self.conn.cursor()
            return self.curr
        except sqlite3.Error as Error:
            print("Error al abrir la base de datos: ", Error)
            return None
    
    def close(self):
        try:
            if self.conn:
                self.conn.commit()
                self.conn.close()
        except sqlite3.Error as Error:
            print("Error al cerrar la base de datos: ", Error)