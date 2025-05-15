"""
NOMBRE PROCESO      :   C2.py
DESCRIPCION PROCESO :   Protege las contraseñas
FECHA CREACION      :   2025-04-01
------------------------------------------------------------------------------------------------
FECHA       DESCRIPCION MODIFICACION                                    MODIFICADO POR
------------------------------------------------------------------------------------------------
"""

import hashlib

class C2():
    def __init__(self, passw, hpassw=None):
        self.crea  = self.__C002a(passw)
        if hpassw is not None:
            self.valida = self.__C002b(passw, hpassw) 
    
    #   ===============================================
    #   .................... Metodos .................. 
    #   ===============================================
    @staticmethod
    def __C002a(Contraseña):
        sha256 = hashlib.sha256()
        sha256.update(Contraseña.encode('utf-8'))
        return sha256.hexdigest()

    @staticmethod
    def __C002b(Contraseña, hashContraseña):
        hash_ingresado = C2.__C002a(Contraseña)
        return hash_ingresado == hashContraseña

