#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
about = '<html><body><h3><center>PyGenRetrieve (version 1.1)</center></h3><p>This is a very simple software for retreiving data from <b>NCBI GTR</b> (Genetic Testing Registry)</p><p>This app uses the libraries: <b><i>pandas, pyqt4, bs4</i></b></p><p>Use is free according to GPL V2.0 or superior.</p><p>Developed by: <a href="mailto:kleydson.stenio@gmail.com?Subject=PyGenRetrieve" target="_top">Kleydson Stenio</a></p></body></html>'
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
		
		# variables
		self.word, self.out, self.pages = '', '', 0
		self.running = False
		
		# connects
		self.word_le.textChanged.connect(self.setWord)
		self.start_pb.clicked.connect(self.startRetrieve)
		self.stop_pb.clicked.connect(lambda : self.start_stop(False))
		self.actionAbout.triggered.connect(self.about)
	
	# methods
	def setWord(self,text):
		out = text.replace(' ','_')+'.txt'
		self.out_le.setText(out)
		self.word, self.out = text, out
	
	def about(self):
		QtGui.QMessageBox.about(self, 'About', about)
	
	# start retrieving
	def startRetrieve(self):
		self.start_stop(True)
		out = pandas.Series(dtype=str)
		do, i = True, 0
		if self.word:
			while (do and self.running):
				try:
					TempDataFrame = pandas.read_html('https://www.ncbi.nlm.nih.gov/gtr/all/genes/?term=%s&page=%d' %(self.word.replace(' ','+'),i+1))
					TempDataFrame2 = TempDataFrame[0].iloc[:, 1].map(lambda x: x.replace('Tests', '').replace('Test', ''))
					out = out.append(TempDataFrame2)
					self.genes_lb.setText('%i' %len(out)); QtGui.QApplication.processEvents()
					i += 1
					if len(TempDataFrame2) < 20: do = False
				except (ValueError,ConnectionRefusedError) as err:
					if type(err) == ValueError:
						QtGui.QMessageBox.critical(self, 'Failed!', 'No genes found.')
					elif type(err) == ConnectionRefusedError:
						QtGui.QMessageBox.critical(self, 'Failed!', 'Connection error.\nTry again in a few moments.')
					self.running = False
		else:
			QtGui.QMessageBox.critical(self, 'Failed!', 'Write a disease before running.')
			self.running = False
		if self.running:
			out.to_csv(self.out, index=False)
			QtGui.QMessageBox.information(self, 'Success!', 'All genes retrieved.\nFile "%s" saved.' %self.out)
		self.start_stop(False)
	
	def start_stop(self,val):
		self.stop_pb.setEnabled(val)
		self.start_pb.setEnabled(not val)
		self.running = val
		self.stop_pb.setStyleSheet('background-color:#bf4040; color:#ffffff;')
		self.genes_lb.setText('0')
		QtGui.QApplication.processEvents()
		QtGui.QApplication.processEvents()
		if not val:
			self.stop_pb.setStyleSheet('')
	
# ################# #
# start application #
# ################# #

application = QtGui.QApplication(sys.argv)
Window = PGR_GUI(None)
Window.show()
application.exec_()
