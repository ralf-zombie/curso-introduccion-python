#! /usr/bin/env python
# -*- coding: utf8 -*-
"""
Ejercicio en QT4
Linux:
(su)
apt-get install python-qt4
apt-get install qt4-designer
apt-get install libqt4-designer
Windows:
https://riverbankcomputing.com/software/pyqt/download

"""
import sys
from PyQt4 import QtCore, QtGui, uic #QtSql para vincular con ddbb SQL
"""
http://doc.qt.io/qt-4.8/examples-sql.html

def conn():
	db = QtSql.QSqlDatabase.addDatabase('QMYSQL')
	db.setHostName('localhost')
	db.setDatabaseName('curso')
	db.setUserName('curso')
	db.setPassword('curso')
	db.open()
	return True

pip install pyinstaller
	
"""
 
# Cargar archivo .ui
form_class = uic.loadUiType("visor.ui")[0]
 
class VentanaQt(QtGui.QMainWindow, form_class):
	# Se define el constructor __init__
	def __init__(self, parent=None):
		QtGui.QMainWindow.__init__(self, parent)
		self.setupUi(self)
		self.setWindowTitle('Primer ejemplo PyQT')
		self.btn.clicked.connect(self.suma)
 
 
# Evento de botón
	def suma(self):
		resultado = int(self.obj_uno.text()) + int(self.obj_dos.text())
		self.res.setText(str(resultado))
 
app = QtGui.QApplication(sys.argv)

MyWindow = VentanaQt(None)
MyWindow.show()
app.exec_()
