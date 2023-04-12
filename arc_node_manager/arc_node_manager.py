# This Python file uses the following encoding: utf-8
import sys
from PySide2.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QListWidget

import os
import rclpy
import threading

from rclpy.node import Node
from os.path import exists
from pathlib import Path

from ament_index_python import get_resource


class MainForm(QWidget):
    def __init__(self):
        super(MainForm, self).__init__()
        self.ini_ros_node()
        self.init_ui()

    def release(self):
        print('release called')
        rclpy.shutdown()
        self.spin_thread.join()

    def ini_ros_node(self):
        rclpy.init(args=sys.argv)
        self.node = rclpy.create_node('node_manager')
        # Spin in a separate thread
        self.spin_thread = threading.Thread(
            target=rclpy.spin, args=(self.node, ), daemon=True)
        self.spin_thread.start()

    def init_ui(self):
        # Create widgets
        btn1 = QPushButton('Button 1')
        btn2 = QPushButton('Button 2')
        btn3 = QPushButton('Button 3')
        lst = QListWidget()

        # Create layouts
        hbox = QHBoxLayout()
        hbox.addWidget(btn1)
        hbox.addWidget(btn2)
        hbox.addWidget(btn3)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox)
        vbox.addWidget(lst)

        # Set main layout
        self.setLayout(vbox)

        # Set window properties
        self.setWindowTitle('Layout Example')
        self.setGeometry(100, 100, 300, 150)

        # Connect signals to slots
        btn1.clicked.connect(lambda: lst.addItem('Button 1 clicked'))
        btn2.clicked.connect(lambda: lst.addItem('Button 2 clicked'))
        btn3.clicked.connect(lambda: lst.addItem('Button 3 clicked'))


def main(args=None):

    app = QApplication(sys.argv)
    ex = MainForm()
    ex.show()
    ret = app.exec_()
    ex.release()
    sys.exit(ret)


main()
