from PyQt5.QtCore import QObject, pyqtSignal

import parametros as p


class LogicaInicio(QObject):

    senal_respuesta_validacion = pyqtSignal(bool, list)
    senal_abrir_juego = pyqtSignal(str)

    def __init__(self):
        super().__init__()

    def comprobar_usuario(self, tupla_respuesta):
        # COMPLETAR
        lista_errores = []
        usuario = tupla_respuesta[0]
        contrasena = tupla_respuesta[1]
        if not usuario.isalnum() or len(usuario)>p.MAX_CARACTERES:
            lista_errores.append("Usuario")
        if contrasena != p.PASSWORD:
            lista_errores.append("Contraseña")

        if contrasena == p.PASSWORD and (usuario.isalnum() and len(usuario)<=p.MAX_CARACTERES):
            self.senal_abrir_juego.emit(usuario)
            self.senal_respuesta_validacion.emit(True, lista_errores)
        else:
            self.senal_respuesta_validacion.emit(False, lista_errores)
