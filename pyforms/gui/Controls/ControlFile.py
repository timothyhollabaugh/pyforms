#!/usr/bin/python
# -*- coding: utf-8 -*-

from pysettings import conf

from pyforms.gui.Controls.ControlText import ControlText

import pyforms.utils.tools as tools

if conf.PYFORMS_USE_QT5:
	from PyQt5.QtWidgets import QFileDialog
	from PyQt5 import uic

else:
	from PyQt4.QtGui import QFileDialog
	from PyQt4 import uic


class ControlFile(ControlText):
	def init_form(self):
		control_path = tools.getFileInSameDirectory(__file__, "fileInput.ui")
		self._form = uic.loadUi(control_path)
		self._form.label.setText(self._label)
		self._form.pushButton.clicked.connect(self.click)
		self.form.lineEdit.editingFinished.connect(self.finishEditing)
		self._form.pushButton.setIcon(conf.PYFORMS_ICON_FILE_OPEN)

	def finishEditing(self):
		"""Function called when the lineEdit widget is edited"""
		self.changed_event()

	def click(self):
		value = QFileDialog.getOpenFileName(self.parent, self._label, self.value)
		
		if conf.PYFORMS_USE_QT5:
			value = value[0]
		else:
			value = str(value)

		if value and len(value)>0: self.value = value

