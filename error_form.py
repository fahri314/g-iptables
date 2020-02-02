# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'error_form.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Error_Form(object):
    def setupUi(self, Error_Form):
        Error_Form.setObjectName("Error_Form")
        Error_Form.resize(561, 63)
        self.textBrowser = QtWidgets.QTextBrowser(Error_Form)
        self.textBrowser.setGeometry(QtCore.QRect(0, 0, 561, 61))
        self.textBrowser.setObjectName("textBrowser")

        self.retranslateUi(Error_Form)
        QtCore.QMetaObject.connectSlotsByName(Error_Form)

    def retranslateUi(self, Error_Form):
        _translate = QtCore.QCoreApplication.translate
        Error_Form.setWindowTitle(_translate("Error_Form", "Form"))

