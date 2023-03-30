#Author Vodohleb04
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'input_name_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from typing import Tuple


class Ui_inputNameDialog(object):
    def setupUi(self, inputNameDialog):
        self._new_record = None
        inputNameDialog.setObjectName("inputNameDialog")
        inputNameDialog.resize(343, 101)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/icons/bimer.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        inputNameDialog.setWindowIcon(icon)
        inputNameDialog.setStyleSheet("background-color: rgb(255, 225, 230);")
        self.inputNameDialogButtonBox = QtWidgets.QDialogButtonBox(inputNameDialog)
        self.inputNameDialogButtonBox.setGeometry(QtCore.QRect(160, 50, 171, 32))
        self.inputNameDialogButtonBox.setStyleSheet("background-color: rgb(199, 214, 255);")
        self.inputNameDialogButtonBox.setOrientation(QtCore.Qt.Horizontal)
        self.inputNameDialogButtonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.inputNameDialogButtonBox.setObjectName("inputNameDialogButtonBox")
        self.inputNameDialogButtonBox.button(self.inputNameDialogButtonBox.StandardButton.Ok).setEnabled(False)
        self.nameLineEdit = QtWidgets.QLineEdit(inputNameDialog)
        self.nameLineEdit.setGeometry(QtCore.QRect(10, 10, 321, 32))
        self.nameLineEdit.setStyleSheet("background-color: rgb(199, 214, 255);")
        self.nameLineEdit.setObjectName("nameLineEdit")

        self.retranslateUi(inputNameDialog)
        self.inputNameDialogButtonBox.accepted.connect(inputNameDialog.accept)
        self.inputNameDialogButtonBox.rejected.connect(inputNameDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(inputNameDialog)

        self.nameLineEdit.textChanged.connect(self.connect_line_edit)
        self.inputNameDialogButtonBox.accepted.connect(self.connect_accepted)

    def retranslateUi(self, inputNameDialog):
        _translate = QtCore.QCoreApplication.translate
        inputNameDialog.setWindowTitle(_translate("inputNameDialog", "Input name"))
        self.nameLineEdit.setPlaceholderText(_translate("inputNameDialog", "Input your name..."))

    def connect_line_edit(self):
        if not self.nameLineEdit.text():
            self.inputNameDialogButtonBox.button(self.inputNameDialogButtonBox.StandardButton.Ok).setEnabled(False)
        else:
            self.inputNameDialogButtonBox.button(self.inputNameDialogButtonBox.StandardButton.Ok).setEnabled(True)

    def connect_accepted(self):
        self._new_record = self.nameLineEdit.text()

    @property
    def new_record(self) -> [Tuple[str, int], None]:
        return self._new_record
