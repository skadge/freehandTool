#!/usr/bin/env python


'''
Qt widget that run the freehand tools

Copyright 2012 Lloyd Konneker, Severin Lemaignan

This is free software, covered by the GNU General Public License.
'''     

from PySide.QtCore import *
from PySide.QtGui import *
import sys

from freehand import FreehandTool

class QFreehandView(QGraphicsView):
  def __init__(self, parent=None):
      super(QFreehandView, self).__init__(parent)
      
      assert self.dragMode() is QGraphicsView.NoDrag
      
      self.setRenderHint(QPainter.Antialiasing)
      self.setRenderHint(QPainter.TextAntialiasing)

      self.setMouseTracking(True);  # Enable mouseMoveEvent
      self.freehandTool = FreehandTool(self.scene(), self)


  ''' Delegate events to FreehandTool. '''
  def mouseMoveEvent(self, event):
    # print "GV mouse moved"
    self.freehandTool.pointerMoveEvent(event)
  
  def mousePressEvent(self, event):
    # print "GV mouse pressed"
    self.freehandTool.pointerPressEvent(event)
    
  def mouseReleaseEvent(self, event):
    self.freehandTool.pointerReleaseEvent(event)
    
  # TESTING
  def keyPressEvent(self, event):
    self.freehandTool.keyPressEvent(event)

