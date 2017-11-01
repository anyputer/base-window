import sys
from PyQt5.QtWidgets import *
    
class AppForm(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()
    
    def initUI(self):
        self.resize(450, 350)
        self.setWindowTitle("Basic Window")

        self.btn = QPushButton("Press me!", self)
        self.btn.move(20, 20)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    window = AppForm()
    window.show()
    
    sys.exit(app.exec_())
