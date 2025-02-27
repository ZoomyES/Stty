import sys
import random
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, 
                            QVBoxLayout, QPushButton, QGraphicsView,
                            QGraphicsScene, QGraphicsEllipseItem)
from PyQt6.QtGui import QBrush, QColor
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Случайные окружности")
        self.setGeometry(100, 100, 600, 500)
        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        
        self.graphics_view = QGraphicsView()
        layout.addWidget(self.graphics_view)
        
        self.add_button = QPushButton("Добавить окружность")
        layout.addWidget(self.add_button)

class CircleWindow(MainWindow):
    def __init__(self):
        super().__init__()
        
        self.scene = QGraphicsScene()
        self.graphics_view.setScene(self.scene)
        
        self.add_button.clicked.connect(self.add_circle)
        
    def add_circle(self):
        diameter = random.randint(10, 100)
        color = QColor(
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255)
        )
        
        view_width = self.graphics_view.width() - diameter
        view_height = self.graphics_view.height() - diameter
        x = random.randint(0, max(0, view_width))
        y = random.randint(0, max(0, view_height))
        
        ellipse = QGraphicsEllipseItem(x, y, diameter, diameter)
        ellipse.setBrush(QBrush(color))
        ellipse.setPen(Qt.PenStyle.NoPen)
        
        self.scene.addItem(ellipse)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CircleWindow()
    window.show()
    sys.exit(app.exec())
