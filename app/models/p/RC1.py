from app.models.p import C1, C2
#   --------------------------------------------------------------------------------------------
Conn = C1.conn()
"""
NOMBRE PROCESO      :   C1.py
DESCRIPCION PROCESO :   Estable conexion a la base de datos
FECHA CREACION      :   2025-04-01
------------------------------------------------------------------------------------------------
FECHA       DESCRIPCION MODIFICACION                                    MODIFICADO POR
------------------------------------------------------------------------------------------------
"""

class RC1():
    def __init__(self, TDOC=None, NDOC=None, PW=None):
        self.TDOC = TDOC
        self.NDOC = NDOC
        self.NOM  = None
        self.APE  = None
        self.FNAC = None
        self.PW   = PW
        self.STAT = None
        self.IMG = None

    def Log_In(self,):
        try:
            curr = Conn.open()
            curr.execute("SELECT RC1PW FROM RC1a WHERE RC1TDOC = ? AND RC1NDOC = ?;", (self.TDOC, self.NDOC))
            PW = curr.fetchone()
            Conn.close()
            if PW:
                if C2.C2(self.PW, PW[0]).valida:
                    return True, ""
                return False, "Credenciales incorrectas"
            return False, "Credenciales incorrectas"
        except Exception as Error:
            print("Error RC1: Log_In - ", Error)
            return False, ""
        
    def Usuario(self):
        try:
            curr = Conn.open()
            curr.execute("SELECT * FROM RC1 WHERE RC1TDOC = ? AND RC1NDOC = ?;", (self.TDOC, self.NDOC))
            Usuario = curr.fetchone()
            Conn.close()
            self.NOM  = Usuario[2]
            self.APE  = Usuario[3]
            self.FNAC = Usuario[4]
            self.IMG  = Usuario[5]
        except Exception as Error:
            print("Error RC1:Usuario - ", Error)
            return False


    def Ingresa(self,):
        try:   
            curr = Conn.open()
            curr.execute("""
            INSERT INTO RC1
                (RC1TDOC, RC1NDOC, RC1NOM, RC1APE, RC1FNAC)
            VALUES
                (?,?,?,?,?)
            ;""", self.TDOC, self.NDOC, self.NOM, self.APE, self.FNAC)
            curr.execute("""
            INSERT INTO RC1a
                (RC1TDOC, RC1NDOC, RC1PW, RC1STAT)
            VALUES
                ?,?,?,?)
            ;""", self.TDOC, self.NDOC, self.PW, self.STAT)
            Conn.close()
        except Exception as Error:
            print("Error RC1:Ingresa - ", Error)

    def Valida(self,):
        pass
    def Actualiza(self,):
        pass

def Log(RQ):
    try:
        if RQ.method == 'POST':
            TDOC = RQ.form.get("TDOC")
            NDOC = RQ.form.get("NDOC")
            PW   = RQ.form.get("PW")
            Usuario = RC1(TDOC, NDOC, PW)
            Login = Usuario.Log_In()
            if Login[0]:
                return True, (TDOC, NDOC)
            else:
                return Login
        return False, ""
    except Exception as Error:
        print("Error RC1:Log - ", Error)
        return False, "Error de conexión"