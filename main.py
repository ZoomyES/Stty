import sys
import random
from PyQt6.QtWidgets import (QApplication, QMainWindow, 
                             QGraphicsScene, QGraphicsEllipseItem)
from PyQt6 import uic
from PyQt6.QtGui import QBrush, QColor
from PyQt6.QtCore import Qt


class CircleWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
   
        uic.loadUi('UI.ui', self)
        
        self.scene = QGraphicsScene()
        self.graphicsView.setScene(self.scene)
        
        self.pushButton.clicked.connect(self.add_circle)
        
    def add_circle(self):
        diameter = random.randint(10, 100)
        
        view_width = self.graphicsView.width() - diameter
        view_height = self.graphicsView.height() - diameter
        x = random.randint(0, view_width) if view_width > 0 else 0
        y = random.randint(0, view_height) if view_height > 0 else 0
        
        ellipse = QGraphicsEllipseItem(x, y, diameter, diameter)
        ellipse.setBrush(QBrush(QColor(255, 255, 0))) 
        
        self.scene.addItem(ellipse)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CircleWindow()
    window.show()
    sys.exit(app.exec_())
