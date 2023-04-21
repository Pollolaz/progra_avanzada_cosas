import os
import sys
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import (QWidget, QApplication, QLabel, QLineEdit,
                             QVBoxLayout, QHBoxLayout, QPushButton,
                             )
from PyQt5.QtGui import QPixmap
import parametros as p

class VentanaInicio(QWidget):

    senal_enviar_login = pyqtSignal(tuple)

    def __init__(self):
        super().__init__()

        # Geometría
        self.setGeometry(600, 200, 500, 500)
        self.setWindowTitle('Ventana de Inicio')
        self.setStyleSheet("background-color: lightblue;")
        self.crear_elementos()

    def crear_elementos(self):
        # CCOMPLETAR
        self.label1 = QLabel(self)
        self.label1.setGeometry(0,0,200,200)
        ruta_imagen = os.path.join("assets", "logo.png")
        pixeles = QPixmap(p.RUTA_LOGO)
        self.label1.setPixmap(pixeles)

        self.label2 = QLabel("Ingrese usuario", self)

        self.edit1 = QLineEdit("", self)

        self.label3 = QLabel("Ingrese contrasena", self)

        self.edit2 = QLineEdit("", self)
        self.edit2.setEchoMode(QLineEdit.Password)

        self.boton = QPushButton("Enviar Login",self)
        self.boton.clicked.connect(self.enviar_login)

        vbox = QVBoxLayout()
        vbox.addWidget(self.label1)
        vbox.addWidget(self.label2)
        vbox.addWidget(self.edit1)
        vbox.addWidget(self.label3)
        vbox.addWidget(self.edit2)
        vbox.addWidget(self.boton)

        self.setLayout(vbox)

        self.show()

    def enviar_login(self):
        # COMPLETAR
        usuario = self.edit1.text()
        contrasena = self.edit2.text()
        self.senal_enviar_login.emit((usuario, contrasena))

    def recibir_validacion(self, valid, errores):
        # COMPLETAR
        if valid:
            self.hide()
        else:
            if "Usuario" in errores:
                self.edit1.setText("Wrong user")
                self.edit1.resize(self.edit1.sizeHint())
            if "Contraseña" in errores:
                self.edit2.setText("Wrong password")
                self.edit2.resize(self.edit1.sizeHint())


if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaInicio()
    ventana.crear_elementos()
    ventana.show()
    sys.exit(app.exec_())
