import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel

class TextOutputApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('문장 출력 앱')
        self.setGeometry(100, 100, 400, 150)

        self.input_label = QLabel('문장을 입력하세요:')
        self.input_text = QLineEdit()
        self.output_label = QLabel('입력한 문장:')
        self.output_text = QLabel()

        self.submit_button = QPushButton('출력')

        layout = QVBoxLayout()
        layout.addWidget(self.input_label)
        layout.addWidget(self.input_text)
        layout.addWidget(self.output_label)
        layout.addWidget(self.output_text)
        layout.addWidget(self.submit_button)

        self.submit_button.clicked.connect(self.displayText)

        self.setLayout(layout)

    def displayText(self):
        input_text = self.input_text.text()
        self.output_text.setText(input_text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TextOutputApp()
    window.show()
    sys.exit(app.exec_())
