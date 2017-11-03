#!/usr/bin/env python3

import argparse
import sys

from PyQt5 import QtWidgets, QtCore, QtGui

from runxtb.gui import Ui_XtbRunnerWindow
from runxtb.handler import handle_gaussian

class XtbRunner(QtWidgets.QMainWindow, Ui_XtbRunnerWindow):
    def __init__(self, coords):
        super(XtbRunner, self).__init__()
        self.setupUi(self)
        self.status_bar = QtWidgets.QStatusBar()
        self.setStatusBar(self.status_bar)

        self.text = ""
        self.coords = coords
        self.check_coords()
        self.geom_lineedit.insert(self.coords)

        self.process = QtCore.QProcess(self)
        self.process.readyRead.connect(self.show_output)

        self.grad_button.clicked.connect(self.grad)
        self.opt_button.clicked.connect(self.opt)
        self.siman_button.clicked.connect(self.siman)

        self.uhf_spinbox.valueChanged.connect(self.update_xtb_line)
        self.charge_spinbox.valueChanged.connect(self.update_xtb_line)
        self.gfn_checkbox.stateChanged.connect(self.update_xtb_line)
        self.molden_checkbox.stateChanged.connect(self.update_xtb_line)
        # Inital update
        self.update_xtb_line()

    def set_status(self, message):
        self.status_bar.showMessage(message, 10000)

    def update_xtb_line(self):
        self.xtbline_lineedit.setText(
            "xtb " + self.coords + " " + " ".join(self.get_args())
        )

    def check_coords(self):
        # Don't do anything when it's a .xyz or coord file
        if self.coords.endswith(".xyz"):
            return

        # Otherwise read the file for further processing
        with open(self.coords) as handle:
            text = handle.read()
        org_coords = self.coords
        if self.coords.endswith(".com") or self.coords.endswith(".gjf"):
            self.coords = handle_gaussian(text, self.coords)
        self.set_status(f"Converted {org_coords} to {self.coords}.")

    def show_output(self):
        self.text += str(self.process.readAll(), encoding="utf-8")
        self.text_edit.setPlainText(self.text)
        self.text_edit.moveCursor(QtGui.QTextCursor.End)

    def get_args(self):
        uhf = str(self.uhf_spinbox.value())
        charge = str(self.charge_spinbox.value())
        args = [self.coords, "-uhf", uhf, "-charge", charge]
        if self.molden_checkbox.isChecked():
            args.append("-molden")
        if self.gfn_checkbox.isChecked():
            args.append("-gfn")
        return args

    def run_xtb(self, arg):
        self.text = ""
        args = (*self.get_args(), arg)
        self.process.start("xtb", args)

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
