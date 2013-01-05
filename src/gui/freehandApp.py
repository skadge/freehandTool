#!/usr/bin/env python


'''
Qt app demonstrating freehand drawing tool.

Copyright 2012 Lloyd Konneker

This is free software, covered by the GNU General Public License.
'''

from PySide.QtCore import *
from PySide.QtGui import *
import sys

from freehand.qt import QFreehandView

class MainWindow(QMainWindow):
    def __init__(self, *args):
        QMainWindow.__init__(self, *args)
        self.scene = QGraphicsScene()
        self.view = QFreehandView(self.scene)
        rect =QRect(-500, -500, 500, 500)
        self.view.fitInView(rect)
        self.view.setSceneRect(rect)
        self.setCentralWidget(self.view)

        
def main(args):
    app = QApplication(args)
    mainWindow = MainWindow()
    mainWindow.setGeometry(100, 100, 500, 500)
    mainWindow.show()

    sys.exit(app.exec_()) # Qt Main loop


if __name__ == "__main__":
    main(sys.argv)
