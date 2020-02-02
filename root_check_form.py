# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'root_check_form.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Root_Check_Form(object):
    def setupUi(self, Root_Check_Form):
        Root_Check_Form.setObjectName("Root_Check_Form")
        Root_Check_Form.resize(254, 80)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Root_Check_Form.sizePolicy().hasHeightForWidth())
        Root_Check_Form.setSizePolicy(sizePolicy)
        self.label = QtWidgets.QLabel(Root_Check_Form)
        self.label.setGeometry(QtCore.QRect(70, 10, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Root_Check_Form)
        self.pushButton.setGeometry(QtCore.QRect(90, 40, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Root_Check_Form)
        QtCore.QMetaObject.connectSlotsByName(Root_Check_Form)

    def retranslateUi(self, Root_Check_Form):
        _translate = QtCore.QCoreApplication.translate
        Root_Check_Form.setWindowTitle(_translate("Root_Check_Form", "Error"))
        self.label.setText(_translate("Root_Check_Form", "You Must Be Root"))
        self.pushButton.setText(_translate("Root_Check_Form", "OK"))

