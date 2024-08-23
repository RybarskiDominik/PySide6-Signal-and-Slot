from PySide6.QtCore import Signal, Qt
from PySide6.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton, QApplication
from NewWindow import NewWindow
import sys

class MainWindow(QMainWindow):
    message_signal = Signal(str)  # Define a signal that emits a string

    def __init__(self):
        super().__init__()
        
        self.new_win = None  # Placeholder for the second window instance

        self.setWindowTitle("Main Window")
        self.setFixedSize(300, 200)

        self.layout = QVBoxLayout()

        self.label = QLabel("Waiting for massenge")
        self.label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.label)

        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)

        self.button = QPushButton("Open New Window")
        self.button.clicked.connect(self.open_new_win)
        self.layout.addWidget(self.button)

    def current_position(self):
        current_position = main_win.geometry()
        new_x = current_position.x() + self.new_win.width()
        title_bar_height = main_win.frameGeometry().height() - main_win.geometry().height()
        new_y = current_position.y() - title_bar_height
        return new_x, new_y
    
    
    def receive_message(self, message):  # Update the label with the received message
        self.label.setText(message)  
        print("Receive!")

    def open_new_win(self):
        if self.new_win is None:
            self.new_win = NewWindow()  # Create NewWindow instance

            # Connect signal from NewWindow to MainWindow
            self.new_win.message_signal.connect(self.receive_message)
            
            x, y = self.current_position()
            self.new_win.move(x, y)
            self.new_win.show()
        else:
            self.new_win.show()
    

if __name__ == "__main__":
    app = QApplication(sys.argv)

    main_win = MainWindow()
    main_win.show()

    sys.exit(app.exec())