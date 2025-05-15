from flask import Blueprint, render_template, request as RQ, redirect as RD, session
from config import Config
#   --------------------------------------------------------------------------------------------
from app.models.p import RC1, RC2

"""
Proyecto realizado por:
    - Fernando Ramos
Contacto: +51 984 165 970
"""

bp = Blueprint("main", __name__)

@bp.route("/", methods=["GET", "POST"])
def _i():
    session.clear()
    Login = RC1.Log(RQ)
    if Login[0]:
        session["user"]    = Login[1]
        session["session"] = True
        return RD("/home")
    return render_template(Config.RT_LOGIN, MENSAJE = Login[1])

@bp.route("/home")
def _home():
    if session.get("session"):
        Usuario    = RC1.RC1(session["user"][0], session["user"][1])
        Integrantes = RC2.RC2()
        Usuario.Usuario()
        print(Usuario, "ss")
        return render_template(Config.RT_HOME, Integrantes = Integrantes.Listar_Integrantes(), Usuario = Usuario)
    return RD("/")


@bp.route("/integrantes")
def _integrantes():
    if session.get("session"):
        Usuario    = RC1.RC1(session["user"][0], session["user"][1])
        Integrantes = RC2.RC2()
        Usuario.Usuario()
        print(Usuario, "ss")
        return render_template(Config.RT_INTEGRANTES, Integrantes = Integrantes.Listar_Integrantes(), Usuario = Usuario)
    return RD("/")