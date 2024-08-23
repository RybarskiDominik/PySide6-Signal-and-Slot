from PySide6.QtCore import Signal, Qt
from PySide6.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton, QApplication
import sys


class NewWindow(QMainWindow):
    message_signal = Signal(str)  # Define a signal that emits a string

    def __init__(self):
        super().__init__()

        self.setWindowTitle("New Window")
        self.setFixedSize(300, 200)

        self.layout = QVBoxLayout()

        self.label = QLabel("This is the New Window.")
        self.label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.label)

        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)

        self.button = QPushButton("Send to Main Window")
        self.button.clicked.connect(self.send_message)
        self.layout.addWidget(self.button)

    def send_message(self):  # Emit the message signal
        message = "Hello from New Window"
        self.message_signal.emit(message)  
        print("Send")

if __name__ == "__main__":
    app = QApplication(sys.argv)

    main_win = NewWindow()
    main_win.show()
    
    sys.exit(app.exec())