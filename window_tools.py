#!/usr/bin/python3
"""
    module
"""

from PyQt5.QtWidgets import (
    QApplication,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QColorDialog,
    QSlider,
    QLabel
)
from PyQt5.QtCore import Qt
import numpy as np

class Button(QPushButton):
    def __init__(self, value, idx, window):
        super().__init__(value)
        self.clicked.connect(self.click)
        self.idx = idx
        self.window = window

    def click(self):
        self.window.idx_changer(self.idx)

class Window(QWidget):
    def __init__(self, lis, idx_changer, color_changer):
        super().__init__()
        self.setWindowTitle("QVBoxLayout Example")
        self.resize(270, 110)
        # Create a QVBoxLayout instance
        layout = QVBoxLayout()
        self.idx_changer = idx_changer
        self.color_changer = color_changer
        layout.addWidget(QLabel("color:"))
        color_button = QPushButton("")
        color_button.clicked.connect(self.select_color)
        color_button.setStyleSheet("""
        QPushButton {
            background-color: rgb(0, 0, 0);
            border-width: 6px;
            border-radius: 10px;
        }""")
        color_button.setGeometry(50, 10, 10, 10)
        self.color_button = color_button
        layout.addWidget(color_button)
        #size_slider = QSlider(Qt.Horizontal, self)
        #size_slider.setGeometry(30, 40, 200, 30)
        #layout.addWidget(size_slider)

        # Add widgets to the layout
        layout.addWidget(QLabel("tools:"))
        for key, value in enumerate(lis):
            b = Button(value, key, self)
            layout.addWidget(b)

        # Set the layout on the application's window
        self.setLayout(layout)

    def select_color(self):
        color = QColorDialog.getColor()
        self.color_changer(color.getRgb()[:3])
        style_text = """
            QPushButton {
                """ + "background-color: rgb{};".format(tuple(color.getRgb()[:3])) + """
                border-width: 6px;
                border-radius: 10px;
            }"""
        self.color_button.setStyleSheet(style_text)

    def change_size(self, value):
        print(value)
