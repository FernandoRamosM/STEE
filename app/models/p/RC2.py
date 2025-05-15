from app.models.p import C1

c = C1.conn()

"""
NOMBRE PROCESO      :   C1.py
DESCRIPCION PROCESO :   Mantenimiento Integrantes
FECHA CREACION      :   2025-04-01
------------------------------------------------------------------------------------------------
FECHA       DESCRIPCION MODIFICACION                                    MODIFICADO POR
------------------------------------------------------------------------------------------------
"""


class RC2():
    def __init__(self, TDOC = None, NDOC = None, NOCOR = None, APOD = None, CARG = None, FNAC = None):
        self.TDOC  = TDOC
        self.NDOC  = NDOC
        self.NOCOR = NOCOR
        self.APOD  = APOD
        self.CARG  = CARG
        self.FNAC  = FNAC
        self.IMG   = None

    def Listar_Integrantes(self,):
        curr = c.open()
        curr.execute("SELECT * FROM RC2 ORDER BY RC2PCARG ASC;")
        Integrantes = curr.fetchall()
        c.close()
        Listado = []

        for Integrante in Integrantes:
            RC1TDOC, RC1NDOC, RC1FNAC, RC2NOCOR, RC2APOD, RC2CARG, RC2PCARG, RC2PIMG = Integrante
            __Integrante = RC2b(RC1TDOC, RC1NDOC)
            __Integrante.Saldo()
            __Integrante.Camiseta()
            __Integrante.NOCOR = RC2NOCOR
            __Integrante.APOD  = RC2APOD
            __Integrante.CARG  = RC2CARG
            __Integrante.FNAC  = RC1FNAC
            __Integrante.IMG   = RC2PIMG
            Listado.append(__Integrante)
        return Listado
    
class RC2a(RC2):
    def __init__(self, TDOC, NDOC):
        super().__init__(TDOC, NDOC)
        self.NOCAM = None
        self.NUCAM = None
        self.TALL = None
        self.OBS = None
    
    def Camiseta(self):
        curr = c.open()
        curr.execute("""
        SELECT
            RC2NOCAM,
            RC2NUCAM,
            RC2TALL,
            RC2OBS
        FROM RC2a
        WHERE
            RC1TDOC = ?
        AND RC1NDOC = ?
        ;""",
        (self.TDOC, self.NDOC))
        RESULTADO = curr.fetchone()
        self.NOCAM = RESULTADO[0]
        self.NUCAM = RESULTADO[1]
        self.TALL = RESULTADO[2]
        self.OBS = RESULTADO[3]
        c.close()

class RC2b(RC2a):
    def __init__(self, TDOC, NDOC):
        super().__init__(TDOC, NDOC)
        self.SDO  = None
        self.TSDO = None

    def Saldo(self):
        curr = c.open()
        curr.execute("""
        SELECT
            RC2SDO
        FROM RC2b 
        WHERE 
            RC1TDOC = ? 
        AND RC1NDOC = ?
        ;""",
        (self.TDOC, self.NDOC))
        RESULTADO = curr.fetchone()
        c.close()
        self.SDO = RESULTADO[0]

    def SaldoT(Self,):
        curr = c.open()
        curr.execute("""
        SELECT
            RC2SDO
        FROM RC2b
        ;""")
        Saldos = curr.fetchall()
        c.close()
        Total = 0
        for Saldo in Saldos:
            Total = Total + Saldo[0]
        return Total
