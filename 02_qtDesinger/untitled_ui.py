# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(608, 575)
        self.button = QtWidgets.QPushButton(Form)
        self.button.setGeometry(QtCore.QRect(250, 310, 93, 28))
        self.button.setObjectName("button")
        self.textEdit = QtWidgets.QPlainTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(13, 6, 571, 281))
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "薪资信息"))
        self.button.setText(_translate("Form", "处理"))
        self.textEdit.setPlaceholderText(_translate("Form", "请输入薪资信息"))
