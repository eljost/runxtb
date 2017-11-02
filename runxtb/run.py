#!/usr/bin/env python3

import argparse
import sys

from PyQt5 import QtWidgets, QtCore, QtGui

from runxtb.gui import Ui_XtbRunnerWindow

class XtbRunner(QtWidgets.QMainWindow, Ui_XtbRunnerWindow):
    def __init__(self, coords):
        super(XtbRunner, self).__init__()
        self.setupUi(self)

        self.coords = coords
        self.geom_lineedit.insert(self.coords)

        self.process = QtCore.QProcess(self)
        self.process.readyRead.connect(self.show_output)

        self.grad_button.clicked.connect(self.grad)
        self.opt_button.clicked.connect(self.opt)
        self.siman_button.clicked.connect(self.siman)

        self.text = ""

    def show_output(self):
        self.text += str(self.process.readAll(), encoding="utf-8")
        self.text_edit.setPlainText(self.text)
        self.text_edit.moveCursor(QtGui.QTextCursor.End)

    def run_xtb(self, arg):
        self.process.start("xtb", (self.coords, arg))

    def grad(self):
        self.run_xtb("-grad")

    def opt(self):
        self.run_xtb("-opt")

    def siman(self):
        self.run_xtb("-siman")


def parse_args(args):
    parser = argparse.ArgumentParser()
    parser.add_argument("coords")

    return parser.parse_args(args)


def main():
    args = parse_args(sys.argv[1:])
    app = QtWidgets.QApplication(sys.argv)
    xtbrunner = XtbRunner(args.coords)
    xtbrunner.show()
    app.exec_()


if __name__ == "__main__":
    main()
