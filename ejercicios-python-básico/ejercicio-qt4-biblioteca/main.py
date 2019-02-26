#!/usr/bin/env python
import sys
from PyQt4 import QtCore, QtGui, uic
from PyQt4.QtGui import *
from PyQt4.QtCore import *

#
ventana = uic.loadUiType("ventana_principal.ui")[0]
agregar = uic.loadUiType("ventana_agregar.ui")[0]
class Agregar(QtGui.QMainWindow, agregar):
	def __init__(self, parent=None):
		QtGui.QMainWindow.__init__(self, parent)
		self.setupUi(self)
		self.setWindowTitle('BiblioSystem')
		self.crearLibro.clicked.connect(self.insert)
	def insert(self):
		QMessageBox.about(self,"AVISO","Ingresando datos de ISBN: <b>"+self.isbn.text()+"</b>")
class VentanaPrincipal(QtGui.QMainWindow, ventana):
    def __init__(self, parent=None):
    	QtGui.QMainWindow.__init__(self, parent)
    	self.setupUi(self)
    	self.setWindowTitle('BiblioSystem')
    	self.agregarLibro.clicked.connect(self.agregar)
    def agregar(self):
        self.ventana = Agregar()
        self.ventana.show()
#
#FUERA DE LA CLASE
app = QtGui.QApplication(sys.argv)
MiVentana = VentanaPrincipal(None)
MiVentana.show()
app.exec_()
