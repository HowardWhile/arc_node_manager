# This Python file uses the following encoding: utf-8
import os
import rclpy
import threading

from rclpy.node import Node
from os.path import exists
from pathlib import Path

from ament_index_python import get_resource
from PySide2.QtWidgets import QApplication
from PySide2.QtWidgets import QWidget
from PySide2.QtCore import QFile
from PySide2.QtUiTools import QUiLoader


class Widget(QWidget):
    def __init__(self):
        super(Widget, self).__init__()
        self.load_ui()

    def load_ui(self):
        loader = QUiLoader()

        ui_file = "form.ui"
        # ui path when run as qt_creator, vscode or `python` command
        ui_path_qt = os.path.join(
            Path(os.path.dirname(__file__)).parent, "resource", ui_file)

        # ui path when run as `ros2 run pkg node`
        _, package_path = get_resource("packages", "arc_node_manager")
        ui_path_ros2 = os.path.join(
            package_path, "share", "arc_node_manager", "resource", "form.ui"
        )

        if exists(ui_path_qt):
            ui_file = QFile(ui_path_qt)

        elif exists(ui_path_ros2):
            ui_file = QFile(ui_path_ros2)

        else:
            print("can not find form.ui from below path")
            print("ui_path_qt:" + ui_path_qt)
            print("ui_path_ros2:" + ui_path_ros2)

        if "ui_file" in locals():
            ui_file.open(QFile.ReadOnly)
            loader.load(ui_file, self)
            ui_file.close()


def main(args=None):
    rclpy.init(args=args)

    node = rclpy.create_node('node_manager')
    # Spin in a separate thread
    thread = threading.Thread(target=rclpy.spin, args=(node, ), daemon=True)
    thread.start()

    app = QApplication([])
    widget = Widget()
    widget.show()
    ret = app.exec_()
    rclpy.shutdown()
    thread.join()


main()
