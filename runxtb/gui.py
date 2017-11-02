# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_XtbRunnerWindow(object):
    def setupUi(self, XtbRunnerWindow):
        XtbRunnerWindow.setObjectName("XtbRunnerWindow")
        XtbRunnerWindow.resize(770, 432)
        self.centralwidget = QtWidgets.QWidget(XtbRunnerWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.geom_label = QtWidgets.QLabel(self.centralwidget)
        self.geom_label.setObjectName("geom_label")
        self.horizontalLayout_3.addWidget(self.geom_label)
        self.geom_lineedit = QtWidgets.QLineEdit(self.centralwidget)
        self.geom_lineedit.setObjectName("geom_lineedit")
        self.horizontalLayout_3.addWidget(self.geom_lineedit)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.text_edit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.text_edit.setObjectName("text_edit")
        self.verticalLayout.addWidget(self.text_edit)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.grad_button = QtWidgets.QPushButton(self.centralwidget)
        self.grad_button.setObjectName("grad_button")
        self.horizontalLayout_2.addWidget(self.grad_button)
        self.opt_button = QtWidgets.QPushButton(self.centralwidget)
        self.opt_button.setObjectName("opt_button")
        self.horizontalLayout_2.addWidget(self.opt_button)
        self.siman_button = QtWidgets.QPushButton(self.centralwidget)
        self.siman_button.setObjectName("siman_button")
        self.horizontalLayout_2.addWidget(self.siman_button)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        XtbRunnerWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(XtbRunnerWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 770, 26))
        self.menubar.setObjectName("menubar")
        XtbRunnerWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(XtbRunnerWindow)
        self.statusbar.setObjectName("statusbar")
        XtbRunnerWindow.setStatusBar(self.statusbar)

        self.retranslateUi(XtbRunnerWindow)
        QtCore.QMetaObject.connectSlotsByName(XtbRunnerWindow)

    def retranslateUi(self, XtbRunnerWindow):
        _translate = QtCore.QCoreApplication.translate
        XtbRunnerWindow.setWindowTitle(_translate("XtbRunnerWindow", "MainWindow"))
        self.geom_label.setText(_translate("XtbRunnerWindow", "Geometry:"))
        self.grad_button.setText(_translate("XtbRunnerWindow", "Grad"))
        self.opt_button.setText(_translate("XtbRunnerWindow", "Opt"))
        self.siman_button.setText(_translate("XtbRunnerWindow", "Siman"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    XtbRunnerWindow = QtWidgets.QMainWindow()
    ui = Ui_XtbRunnerWindow()
    ui.setupUi(XtbRunnerWindow)
    XtbRunnerWindow.show()
    sys.exit(app.exec_())

