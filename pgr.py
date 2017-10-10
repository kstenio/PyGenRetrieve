#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  pgr.py
#
#  Copyright 2017 Kleydson Stenio <kleydson.stenio@gmail.com>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
# In order to the app work, install: python3-pandas, python3-html5lib, python3-bs4, python3-pyqt4
#

# ####### #
# imports #
# ####### #
import pandas, sys
from PyQt4 import QtCore, QtGui, uic

# ############# #
# importing GUI #
# ############# #
interface = uic.loadUiType('./pgr.ui')[0]

# ######### #
# app class #
# ######### #
class PGR_GUI(QtGui.QMainWindow, interface):
	# inicializa a classe/programa
	def __init__(self, parent=None):
		# load all data from GUI
		QtGui.QMainWindow.__init__(self, parent)
		self.setupUi(self)
		self.progressbar.setVisible(False)
		
		# variables
		self.word, self.out, self.pages = '', '', 0
		self.running = False
		
		# connects
		self.word_le.textChanged.connect(self.setWord)
		self.out_le.textChanged.connect(self.setOut)
		self.pages_sb.valueChanged.connect(self.setPages)
		self.start_pb.clicked.connect(self.startRetrieve)
		self.stop_pb.clicked.connect(lambda : self.start_stop(False))
	
	# methods
	def setWord(self,text):
		self.word = text
	
	def setOut(self,text):
		self.out = text
	
	def setPages(self,num):
		self.progressbar.setValue(0)
		self.pages = num
		self.progressbar.setRange(0, num)
	
	def startRetrieve(self):
		self.start_stop(True)
		i, out = 0, pandas.Series(dtype=str)
		while (i < self.pages and self.running == True):
			try:
				TempDataFrame = pandas.read_html('https://www.ncbi.nlm.nih.gov/gtr/all/genes/?term=%s&page=%d' %(self.word.replace(' ','+'),i+1))
				TempDataFrame2 = TempDataFrame[0].iloc[:, 1].map(lambda x: x.replace('Tests', '').replace('Test', ''))
				out = out.append(TempDataFrame2)
				self.progressbar.setValue(i + 1)
				QtGui.QApplication.processEvents()
				i += 1
				if len(TempDataFrame2) < 20: break
			except ValueError:
				QtGui.QMessageBox.question(self, 'Failed!', 'No genes found.', QtGui.QMessageBox.Ok)
				self.running = False
		if self.running:
			out.to_csv(self.out + '.txt', index=False)
			QtGui.QMessageBox.question(self, 'Success!', 'All genes retrieved.', QtGui.QMessageBox.Ok)
		self.start_stop(False)
	
	def start_stop(self,val):
		self.progressbar.setVisible(val)
		self.stop_pb.setEnabled(val)
		self.start_pb.setEnabled(not val)
		self.running = val
		self.stop_pb.setStyleSheet('background-color:#bf4040; color:#ffffff;')
		QtGui.QApplication.processEvents()
		QtGui.QApplication.processEvents()
		if not val:
			self.progressbar.setValue(0)
			self.stop_pb.setStyleSheet('')
		
# ################# #
# start application #
# ################# #

application = QtGui.QApplication(sys.argv)
Window = PGR_GUI(None)
Window.show()
application.exec_()
