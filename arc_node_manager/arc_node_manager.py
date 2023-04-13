# This Python file uses the following encoding: utf-8

# system module
import sys
import threading

# ui module
from PySide2.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QListWidget

# ros module
import rclpy
from std_msgs.msg import String


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

        self.publisher = self.node.create_publisher(String, 'topic', 10)

        self.subscription = self.node.create_subscription(
            String, 'topic', self.listener_callback, 10)

    def init_ui(self):
        # Create widgets
        self.btn_test = QPushButton('Button Test')
        self.btn2 = QPushButton('Button 2')
        self.btn3 = QPushButton('Button 3')
        self.lst = QListWidget()

        # Create layout
        hbox = QHBoxLayout()
        hbox.addWidget(self.btn_test)
        hbox.addWidget(self.btn2)
        hbox.addWidget(self.btn3)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox)
        vbox.addWidget(self.lst)

        # Set main layout
        self.setLayout(vbox)

        # Set window properties
        self.setWindowTitle('Layout Example')
        self.setGeometry(50, 50, 800, 600)

        # Connect signals to slots
        # btn1.clicked.connect(lambda: lst.addItem('Button 1 clicked'))
        # btn2.clicked.connect(lambda: lst.addItem('Button 2 clicked'))
        # btn3.clicked.connect(lambda: lst.addItem('Button 3 clicked'))
        self.btn_test.clicked.connect(self.btn1_clicked)
        self.btn2.clicked.connect(self.btn2_clicked)
        self.btn3.clicked.connect(self.btn3_clicked)

    def btn1_clicked(self):
        msg = String()
        msg.data = 'Button 1 clicked'
        self.publisher.publish(msg)

    def btn2_clicked(self):
        self.lst.addItem('Button 2 clicked')

    def btn3_clicked(self):
        self.lst.addItem('Button 3 clicked')

    def listener_callback(self, msg):
        self.lst.addItem(f"I heard: {msg.data}")
        self.lst.scrollToBottom()


def main(args=None):

    app = QApplication(sys.argv)
    ex = MainForm()
    ex.show()
    ret = app.exec_()
    ex.release()
    sys.exit(ret)


main()
