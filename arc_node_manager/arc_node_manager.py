# This Python file uses the following encoding: utf-8
import os
from pathlib import Path
import sys

from PySide2.QtWidgets import QApplication, QWidget
from PySide2.QtCore import QFile
from PySide2.QtUiTools import QUiLoader

from os.path import exists


class Widget(QWidget):
    def __init__(self):
        super(Widget, self).__init__()
        self.load_ui()

    def load_ui(self):
        loader = QUiLoader()

        ui_path_qt = os.fspath(Path(os.path.dirname(__file__)) / "form.ui")

        # /ros2_ws/install/arc_node_manager/lib/python3.10/site-packages/arc_node_manager/form.ui
        # -> /ros2_ws/install/arc_node_manager/share/arc_node_manager/form.ui
        ui_path_ros2 = os.fspath(
            Path(os.path.dirname(__file__)).parent.parent.parent.parent
            / "share/arc_node_manager/form.ui"
        )

        if exists(ui_path_qt) == True:
            ui_file = QFile(ui_path_qt)
        elif exists(ui_path_ros2) == True:
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
    # rclpy.init(args=args)
    app = QApplication([])
    widget = Widget()
    widget.show()
    sys.exit(app.exec_())
    # rclpy.shutdown()


if __name__ == "__main__":
    main()
