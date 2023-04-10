# This Python file uses the following encoding: utf-8
import os
from pathlib import Path
import sys

from PySide2.QtWidgets import QApplication, QWidget
from PySide2.QtCore import QFile
from PySide2.QtUiTools import QUiLoader


class Widget(QWidget):
    def __init__(self):
        super(Widget, self).__init__()
        self.load_ui()

    def load_ui(self):
        print("[debug]: "+__file__);
        loader = QUiLoader()     
        
        path = os.fspath(Path("/home/user/ros2_ws/src/arc_node_manager/arc_node_manager/arc_node_manager.py").resolve().parent / "form.ui")
        ui_file = QFile(path)
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

