# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'path.ui'
#
# Created: Fri Aug 29 16:14:59 2014
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

#from PySide import QtCore, QtGui
from PyQt4 import QtCore, QtGui

class Ui_PathDialog(object):
    def setupUi(self, PathDialog):
        PathDialog.setObjectName("PathDialog")
        PathDialog.resize(400, 95)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(PathDialog.sizePolicy().hasHeightForWidth())
        PathDialog.setSizePolicy(sizePolicy)
        PathDialog.setMinimumSize(QtCore.QSize(400, 95))
        PathDialog.setMaximumSize(QtCore.QSize(400, 95))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/wow_rogue.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        PathDialog.setWindowIcon(icon)
        self.buttonBox = QtGui.QDialogButtonBox(PathDialog)
        self.buttonBox.setGeometry(QtCore.QRect(50, 60, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.hostsDir = QtGui.QLineEdit(PathDialog)
        self.hostsDir.setGeometry(QtCore.QRect(10, 30, 381, 22))
        self.hostsDir.setObjectName("hostsDir")
        self.label = QtGui.QLabel(PathDialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 111, 16))
        self.label.setObjectName("label")

        self.retranslateUi(PathDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), PathDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), PathDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(PathDialog)

    def retranslateUi(self, PathDialog):
        PathDialog.setWindowTitle(QtGui.QApplication.translate("PathDialog", "Settings - Path", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("PathDialog", "Hosts Directory", None, QtGui.QApplication.UnicodeUTF8))

